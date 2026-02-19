#!/bin/bash
# Sol Therapy - Deploy to GitHub Pages
# Usage: ./deploy.sh
# Requires: git, gh CLI authenticated

set -e

SITE_DIR="/Users/yaronamor/Documents/yaronamor-vault/sol/O-output/website-sol-therapy"
DEPLOY_DIR="/tmp/sol-therapy-deploy"
REPO="yarondeepa-hub/sol-therapy"

echo "=== Sol Therapy Deploy ==="
echo "Source: $SITE_DIR"
echo "Target: https://yarondeepa-hub.github.io/sol-therapy/"
echo ""

# Clean and prepare deploy directory
rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"

# Clone existing repo (preserves git history)
git clone "https://github.com/$REPO.git" "$DEPLOY_DIR"

# Remove old files (except .git)
cd "$DEPLOY_DIR"
for f in *; do
  [ "$f" = ".git" ] && continue
  rm -rf "$f"
done
for f in .[!.]*; do
  [ "$f" = ".git" ] && continue
  rm -rf "$f" 2>/dev/null || true
done
cd -

# Copy site files, excluding non-deploy files
rsync -av \
  --exclude='.netlify' \
  --exclude='*-original.mp4' \
  --exclude='*-backup.html' \
  --exclude='*-pre-*.html' \
  --exclude='*.md' \
  --exclude='.DS_Store' \
  --exclude='deploy.sh' \
  --exclude='images/' \
  --exclude='assets/video/' \
  --exclude='assets/audio/' \
  "$SITE_DIR/" "$DEPLOY_DIR/"

# Remove any remaining unwanted files
rm -f "$DEPLOY_DIR"/index-v*.html
rm -rf "$DEPLOY_DIR"/.netlify

cd "$DEPLOY_DIR"

# Check size
TOTAL_SIZE=$(du -sh -I .git . 2>/dev/null | cut -f1 || du -sh . | cut -f1)
echo "Deploy size: $TOTAL_SIZE"

# Check for files over 100MB (GitHub limit)
LARGE_FILES=$(find . -not -path './.git/*' -type f -size +100M 2>/dev/null)
if [ -n "$LARGE_FILES" ]; then
  echo "ERROR: Files over 100MB found (GitHub limit):"
  echo "$LARGE_FILES"
  exit 1
fi

# Commit and push
git add -A
if git diff --cached --quiet; then
  echo "No changes to deploy."
else
  git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M')"
  git push origin main
  echo ""
  echo "Deployed successfully."
  echo "Site will update in ~30 seconds at:"
  echo "https://yarondeepa-hub.github.io/sol-therapy/"
fi
