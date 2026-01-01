#!/bin/zsh
set -euo pipefail

# Resolve repo directory from this script's location (no hardcoded local path).
REPO_DIR="${0:A:h}"
PYTHON="${REPO_DIR}/venv/bin/python"
SCRIPT="${REPO_DIR}/rotate_scenes.py"

# Ensure consistent relative behavior (even though rotate_scenes.py is now cwd-independent).
cd "${REPO_DIR}"

"${PYTHON}" "${SCRIPT}"


