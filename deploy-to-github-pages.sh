#!/usr/bin/env bash

echo ""
echo "Deploying to github pages..."
echo ""

# Build the book from src dir
mdbook build

# Checkout to gh-pages dir
git checkout gh-pages

# Rename book dir to docs
mv book docs

# Add to git
git add .

# Commit
git commit -m "adding updated website"

# Push to deploy
git push origin gh-pages

# Switch back to last branch
git checkout -
