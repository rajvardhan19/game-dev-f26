"""Exercise the adapter against its own engine process, never a training run."""
import signal
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import json
import time

from server import RANDOM_SEEDS, Session, Watch, snapshot, spend_preview, war_seed


def wait(watch, limit=90):
    end = time.monotonic() + limit
    while watch.state()['status'] == 'running' and time.monotonic() < end:
        time.sleep(0.05)
    return watch.state()


class BridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="cws-ui-test-")
        cls.snapshot = Path(cls.temp.name).resolve()
        snapshot(cls.snapshot)
        sys.path.insert(0, str(cls.snapshot))
        from cws.client import EngineProcess
        cls.EngineProcess = EngineProcess

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.engine = self.EngineProcess()
        self.addCleanup(self.engine.close)
        self.session = Session(self.engine)

    def test_process_uses_temporary_copy(self):
        from cws import client
        self.assertEqual(client.ROOT, self.snapshot)
        self.assertNotEqual(client.ROOT, Path(__file__).resolve().parents[1])

    def test_recruit_and_resolve(self):
        _, state = self.session.mutate('/api/step', {'revision': 0, 'action': 'troops'})
        recruit = next(a for a in state['legal'] if a.startswith('recruit '))
        cash = state['observation']['treasury']['Union']['cash']
        _, state = self.session.mutate('/api/step', {'revision': 1, 'action': recruit})
        self.assertTrue(state['accepted'])
        self.assertEqual(state['observation']['treasury']['Union']['cash'], cash - 100)
        _, state = self.session.mutate('/api/step', {'revision': 2, 'action': 'end turn'})
        self.assertEqual(state['observation']['turn'], 2)
        self.assertTrue(state['observation']['last_turn_report'])

    def test_stale_revision_does_not_repeat_move(self):
        self.session.mutate('/api/step', {'revision': 0, 'action': 'end turn'})
        code, state = self.session.mutate('/api/step', {'revision': 0, 'action': 'end turn'})
        self.assertEqual(code, 409)
        self.assertEqual(state['observation']['turn'], 2)
        self.assertEqual(state['outcome']['steps'], 1)

    def test_reset_alternate_and_no_hidden_enemy_fields(self):
        _, state = self.session.mutate('/api/new', {'revision': 0, 'scenario': 'alternate'})
        self.assertEqual(state['scenario'], 'alternate')
        self.assertEqual(state['observation']['date'], 'April 1861')
        self.assertNotIn('seed', state['observation'])
        for army in state['observation']['enemy_armies']:
            self.assertFalse({'leader','experience','supply','order'} & army.keys())

    def test_invalid_order_is_refused_without_spending(self):
        before = self.session.state()['observation']
        _, state = self.session.mutate('/api/step', {'revision': 0, 'action': 'move 1 Atlantis'})
        self.assertFalse(state['accepted'])
        self.assertEqual(state['observation'], before)

    def test_random_and_practice_wars(self):
        _, state = self.session.mutate('/api/new', {'revision': 0, 'scenario': 'standard', 'war': 'random'})
        self.assertEqual(state['war'], 'a new random war')
        self.assertNotIn('seed', state['observation'])
        self.assertNotIn('seed', state['outcome'])
        _, state = self.session.mutate('/api/new', {'revision': 1, 'scenario': 'alternate', 'war': 103})
        self.assertEqual((state['war'], state['scenario']), ('practice war 103', 'alternate'))

    def test_random_seeds_avoid_every_declared_split(self):
        splits = {1, 2} | set(range(3, 21)) | set(range(101, 105)) | set(range(201, 209)) | set(range(301, 351))
        for _ in range(200):
            seed, _ = war_seed('random')
            self.assertTrue(RANDOM_SEEDS[0] <= seed <= RANDOM_SEEDS[1])
            self.assertNotIn(seed, splits)

    def test_evaluation_and_training_seeds_are_refused(self):
        for war in (1, 2, 201, 301, 105, '101', True, None):
            with self.assertRaises(ValueError):
                self.session.mutate('/api/new', {'revision': 0, 'scenario': 'standard', 'war': war})
        self.assertEqual(self.session.revision, 0)           # nothing changed

    def test_preview_prices_are_what_the_engine_charges(self):
        _, state = self.session.mutate('/api/step', {'revision': 0, 'action': 'troops'})
        revision, spent, checked = 1, 0, []
        for verb in ('recruit ', 'fortify ', 'build wooden'):
            action = next(a for a in state['legal'] if a.startswith(verb))
            price, cash = state['preview']['costs'][action], state['observation']['treasury']['Union']['cash']
            _, state = self.session.mutate('/api/step', {'revision': revision, 'action': action})
            revision += 1
            self.assertTrue(state['accepted'], action)
            self.assertEqual(cash - state['observation']['treasury']['Union']['cash'], price, action)
            spent += price
            self.assertEqual(state['preview']['spent'], spent)
            checked.append((action, price))
        self.assertEqual([p for _, p in checked], [100, 200, 100])
        self.assertEqual(state['preview']['costs']['end turn'], 0)
        _, state = self.session.mutate('/api/step', {'revision': revision, 'action': 'end turn'})
        self.assertEqual(state['preview']['spent'], 0)                       # a new turn starts afresh

    def test_supply_price_matches_resupply(self):
        from cws.interface import CivilWarEpisode
        for seed, cash in ((101, 525), (102, 333), (103, 47)):
            def fresh():
                ep = CivilWarEpisode('standard')
                ep.reset(seed)
                for i in (1, 2, 4):
                    ep._game.supply[i] = 1
                ep._game.cash[1] = cash
                return ep
            ep = fresh()
            preview = spend_preview(ep.observe('union'), ep.legal_actions('union'), 0)
            orders = [a for a in ep.legal_actions('union') if a.startswith('supply ')]
            self.assertTrue(orders or cash < 100)
            for action in orders:
                ep = fresh()
                ep.step('union', action)
                self.assertEqual(cash - ep._game.cash[1], preview['costs'][action], (seed, action))

    def test_upkeep_estimate_is_what_iterate_charges(self):
        from cws.interface import CivilWarEpisode
        for scenario in ('standard', 'alternate'):
            for seed in (101, 102):
                for cash in (None, 150, 40):
                    for cut_off in (False, True):
                        ep = CivilWarEpisode(scenario)
                        ep.reset(seed)
                        g = ep._game
                        if cash is not None:
                            g.cash[1] = cash
                        if cut_off:                                          # an army behind enemy lines
                            i = next(i for i in range(1, 21) if g.armyloc[i] > 0)
                            g.armyloc[i] = next(c for c in range(1, 41) if g.cityp[c] == 2 and g.cutoff(1, c) < 1)
                        estimate = spend_preview(ep.observe('union'), ep.legal_actions('union'), 0)['upkeep']
                        before = g.cash[1]
                        g.iterate()
                        self.assertEqual(before - g.cash[1], estimate, (scenario, seed, cash, cut_off))

    def test_watch_the_1998_ai_play_a_whole_war(self):
        watch = Watch(live=False)
        watch.start({'who': 'original-ai', 'scenario': 'alternate', 'war': 101, 'pace': 0})
        state = wait(watch)
        self.assertEqual(state['status'], 'done')
        self.assertTrue(state['summary']['reason'])
        self.assertIn(state['summary']['tier'], ('win', 'held out', 'decisive loss'))
        actions = [e for e in state['events'] if e['kind'] == 'action']
        self.assertTrue(actions and {e['source'] for e in actions} <= {'scripted', 'fallback'})
        self.assertEqual(state['events'][-1]['kind'], 'end')
        self.assertTrue(state['observation']['cities'])
        self.assertNotIn('seed', json.dumps(state))
        for army in state['observation']['enemy_armies']:
            self.assertFalse({'leader', 'experience', 'supply', 'order'} & army.keys())
        self.assertEqual(watch.state(len(state['events']))['events'], [])   # polling returns only new events

    def test_watch_refuses_paid_players_and_held_out_seeds(self):
        watch = Watch(live=False)
        with self.assertRaises(ValueError):
            watch.start({'who': 'gemini-h', 'scenario': 'standard', 'war': 101})
        for war in (1, 2, 301):
            with self.assertRaises(ValueError):
                watch.start({'who': 'original-ai', 'scenario': 'standard', 'war': war})
        self.assertEqual(watch.state()['status'], 'idle')

    def test_stop_ends_a_watched_war(self):
        watch = Watch(live=False)
        watch.start({'who': 'original-ai', 'scenario': 'standard', 'war': 102, 'pace': 0.05})
        time.sleep(0.5)
        watch.stop = True
        self.assertEqual(wait(watch)['status'], 'stopped')


class Shutdown(unittest.TestCase):
    def test_sigterm_removes_the_snapshot(self):
        with socket.socket() as s:
            s.bind(('127.0.0.1', 0))
            port = s.getsockname()[1]
        temp = Path(tempfile.gettempdir())
        before = set(temp.glob('cws-play-ui-*'))
        server = subprocess.Popen([sys.executable, str(Path(__file__).with_name('server.py')), '--port', str(port)],
                                  stdout=subprocess.PIPE, text=True)
        try:
            self.assertIn(f'127.0.0.1:{port}', server.stdout.readline())
            self.assertTrue(set(temp.glob('cws-play-ui-*')) - before)
            server.send_signal(signal.SIGTERM)
            server.wait(timeout=15)
        finally:
            server.kill()
            server.stdout.close()
        self.assertEqual(set(temp.glob('cws-play-ui-*')) - before, set())


if __name__ == '__main__':
    unittest.main()
