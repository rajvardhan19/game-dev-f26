"""Export the implementation agent's Claude Code session as readable, redacted Markdown.

    python3 tools/export_session.py [--transcript PATH] [--out docs/agent-session.md]

Run it from the project folder before committing, so the export includes the latest turns.

- **Kept:** the student's messages, the agent's replies, every tool call, and the start of each tool result.
- **Removed:** injected system context, internal records and images.
- **Redacted, generic rules:** email addresses, home paths, temporary paths, billing-account IDs, long ID numbers,
  API keys and cloud project tables.
- **Redacted, personal strings:** listed in the git-ignored `.env.redact`, so this file names none of them.

Without --transcript it reads the newest session of this project under ~/.claude/projects/.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERIC = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", "[secret]"),
    (r"AIza[0-9A-Za-z_-]{20,}|sk-[A-Za-z0-9_-]{20,}|ya29\.[0-9A-Za-z_-]{10,}|gh[pousr]_[0-9A-Za-z]{20,}", "[secret]"),
    (r"[\w.+\\-]+@(?:[\w-]+|\[[\w ]+\])(?:\\*\.[\w-]+)+", "[email]"),  # also a\.b@c\.com and a.b@[work].com
    (r"/(?:Users|home)/[^/\s'\"`]+", "~"),
    (r"/private/tmp/claude-\d+/[^\s'\"`)]*", "[temporary path]"),
    (r"/var/folders/[^\s'\"`)]*", "[temporary path]"),
    (r"\b[0-9A-F]{6}-[0-9A-F]{6}-[0-9A-F]{6}\b", "[billing account]"),
    (r"(?m)^[a-z][a-z0-9-]+\s{2,}.+\s\d{6,}\s*$", "[cloud project row]"),
    (r"(?m)^[a-z][a-z0-9-]+\s{2,}(True|False)\s*$", "[cloud project row]"),
    (r"\d{9,}", "[number]"),
]
SYSTEM = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
PASTED = re.compile(r"(<pasted_content[^>]*>)(.*?)(</pasted_content[^>]*>)", re.S)


def load_rules():
    """Secrets and emails first, so a local term never splits an address; then the local terms in file order."""
    rules = [(re.compile(p, re.S), r) for p, r in GENERIC]
    local, terms = ROOT / ".env.redact", []
    if local.exists():
        for line in local.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                term, _, rep = (part.strip() for part in line.partition("=>"))
                terms.append((re.compile(re.escape(term), re.I), rep or "[redacted]"))
    return rules[:3] + terms + rules[3:]


def newest_transcript():
    base = Path.home() / ".claude" / "projects"
    found = sorted(base.glob(f"*{ROOT.parent.name}*/*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not found:
        raise SystemExit(f"no session transcript under {base}; pass --transcript")
    return found[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--transcript", type=Path)
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "agent-session.md")
    args = ap.parse_args()
    rules = load_rules()

    def clean(text, limit=None):
        text = SYSTEM.sub("", text)
        text = PASTED.sub(lambda m: m.group(1) + (m.group(2)[:600] + " … [pasted material shortened]"
                                                  if len(m.group(2)) > 600 else m.group(2)) + m.group(3), text)
        for pat, rep in rules:
            text = pat.sub(rep, text)
        text = text.strip()
        if limit and len(text) > limit:
            text = text[:limit] + f"\n… [{len(text) - limit:,} more characters]"
        return text

    def fence(text):
        return "```\n" + text.replace("```", "ʼʼʼ") + "\n```"

    def tool_input(name, inp):
        if name == "Bash":
            return fence(clean(inp.get("command", ""), 1500))
        if name in ("Write", "Edit"):
            body = inp.get("content") or inp.get("new_string") or ""
            return f"`{clean(inp.get('file_path', ''))}`\n" + fence(clean(body, 800))
        return fence(clean(json.dumps(inp, ensure_ascii=False), 600))

    def result_text(content):
        if isinstance(content, str):
            return content
        return "\n".join(c.get("text", "") if c.get("type") == "text" else "[image]"
                         for c in content or [] if c.get("type") in ("text", "image"))

    src = args.transcript or newest_transcript()
    lines = ["# Implementation agent session",
             "",
             "Claude Code in VS Code (`claude-opus-5-5`): the one long session that built this midterm with the student,",
             f"exported by `tools/export_session.py`. The project's decisions are in AGENT-TEAM.md and SUITE.md.",
             "",
             "- **Kept:** the student's messages, the agent's replies, every tool call, and the start of each tool",
             "  result (long outputs are cut).",
             "- **Removed:** injected system context, internal records and images.",
             "- **Redacted:** emails, paths, account and project identifiers.",
             ""]
    day = None
    for raw in src.open():
        try:
            r = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if r.get("type") not in ("user", "assistant"):
            continue
        ts = (r.get("timestamp") or "")[:10]
        if ts and ts != day:
            day = ts
            lines += ["", f"## {day}", ""]
        content = (r.get("message") or {}).get("content")
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        for c in content or []:
            kind = c.get("type")
            if kind == "text":
                text = clean(c.get("text", ""), 6000 if r["type"] == "assistant" else 4000)
                if text:
                    who = "**Student:**" if r["type"] == "user" else "**Agent:**"
                    if r.get("isCompactSummary"):
                        who = "**[Context summary after compaction]**"
                    lines += [who, "", text, ""]
            elif kind == "tool_use":
                lines += [f"*Tool call: {c.get('name')}*", tool_input(c.get("name"), c.get("input") or {}), ""]
            elif kind == "tool_result":
                text = clean(result_text(c.get("content")), 1200)
                if text:
                    lines += ["*Result:*", fence(text), ""]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n")
    print(f"wrote {args.out.relative_to(ROOT) if args.out.is_relative_to(ROOT) else args.out} "
          f"({args.out.stat().st_size / 1e6:.1f} MB) from {src.name}")


if __name__ == "__main__":
    main()
