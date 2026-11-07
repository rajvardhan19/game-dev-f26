#!/bin/sh
# Train a lessons notebook, freeze it, write its journal and check it on the development seeds, unattended.
#
#   tools/learn_pipeline.sh NAME RUN SEEDS [train flags...]
#   tools/learn_pipeline.sh gemini-c learn-20261026-c 301-350 --mirror --track-record --actionable \
#       --reference learn-20261026-b-reference
#
# Paid calls (Gemini on Vertex AI). Progress: results/RUN/status.md, every 10 games.
# Reads the Vertex settings from .env if present. Stops at the first failure.
set -eu
cd "$(dirname "$0")/.."
[ -f .env ] && { set -a; . ./.env; set +a; }
name=$1 run=$2 seeds=$3
shift 3
uv run --extra live python -m cws.learn train --book "lessons/$name.json" --run "$run" --seeds "$seeds" \
    --max-cost 8 --live "$@"
python3 -m cws.learn freeze --book "lessons/$name.json"
python3 -m cws.learn journal --book "lessons/$name.json" --run "$run"
uv run --extra live python -m cws.evaluate --players model-lessons --lessons "lessons/$name.json" --split dev \
    --live --run "dev-$run" --quiet
echo "done: results/$run/status.md, results/$run/journal.md, results/dev-$run/table.md"
