#!/bin/sh
# Copy this project into a clone of the course repository for submission.
#
#   tools/sync_to_course_repo.sh /path/to/game-dev-f26
#
# Copies everything except local environments and QB64 build outputs into
# midterms/rajvardhan19/, installs the CI workflow, and runs the tests there.
# This folder is the source of truth: --delete removes anything that exists
# only in the course-repo copy, so make every edit here. It never commits or pushes.
set -eu
here=$(cd "$(dirname "$0")/.." && pwd)
repo=${1:?usage: tools/sync_to_course_repo.sh /path/to/game-dev-f26}
dest="$repo/midterms/rajvardhan19"
[ -d "$repo/.git" ] || { echo "not a git clone: $repo" >&2; exit 1; }
mkdir -p "$dest" "$repo/.github/workflows"
rsync -a --delete \
  --exclude '.venv/' --exclude '__pycache__/' --exclude '.DS_Store' \
  --exclude 'tools/qb64-harness/harness' --exclude 'tools/qb64-harness/harness_debug' \
  --exclude 'tools/qb64-harness/harness.bas' --exclude 'tools/qb64-harness/harness_debug.bas' \
  --exclude 'tools/qb64-harness/*_start.command' \
  "$here/" "$dest/"
cp "$here/ci/midterm-rajvardhan19.yml" "$repo/.github/workflows/midterm-rajvardhan19.yml"
cd "$dest" && python3 -m unittest discover -s tests
echo "Synced to $dest. Review with: git -C \"$repo\" status"
