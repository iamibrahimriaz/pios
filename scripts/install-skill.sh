#!/usr/bin/env bash
#
# Install the /pios skill globally, so it works in any project on this machine.
#
#   ./scripts/install-skill.sh
#
# You do NOT need this to use the framework. Working inside the framework
# repository already gives you /pios. This is only for running research from
# some other project directory.
#
# See USAGE.md.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$HOME/.claude/skills"

if [ ! -f "$REPO/framework/engine/run-order.yaml" ]; then
  echo "error: $REPO does not look like the Product Intelligence OS repository." >&2
  exit 1
fi

echo "Framework:  $REPO"
echo "Installing: $DEST/pios"
echo

mkdir -p "$DEST"

if [ -e "$DEST/pios" ] && [ ! -L "$DEST/pios" ]; then
  echo "error: $DEST/pios already exists and is not a symlink." >&2
  echo "Remove or rename it, then run this again." >&2
  exit 1
fi

# A symlink rather than a copy, so `git pull` updates the installed skill too.
ln -sfn "$REPO/skills/pios" "$DEST/pios"
echo "Linked $DEST/pios -> $REPO/skills/pios"
echo

# Work out which profile to suggest.
case "${SHELL##*/}" in
  zsh)  PROFILE="$HOME/.zshrc" ;;
  bash) PROFILE="$HOME/.bashrc" ;;
  fish) PROFILE="$HOME/.config/fish/config.fish" ;;
  *)    PROFILE="your shell profile" ;;
esac

if [ "${SHELL##*/}" = "fish" ]; then
  LINE="set -gx PIOS_HOME \"$REPO\""
else
  LINE="export PIOS_HOME=\"$REPO\""
fi

if [ "${PIOS_HOME:-}" = "$REPO" ]; then
  echo "PIOS_HOME is already set correctly."
else
  echo "One step left. Add this to $PROFILE:"
  echo
  echo "    $LINE"
  echo
  echo "Then restart your terminal, or run it once in the current session."
fi

echo
echo "Verify with:"
echo "    echo \$PIOS_HOME"
echo "    python3 \"$REPO/framework/engine/validate.py\""
echo
echo "Then, from any project directory, invoke /pios in Claude Code."
echo "Runs will be written to ./pios/<slug>/ in whichever project you are in."
