#!/bin/bash

# https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
set -e -x -v -u -o pipefail

# source ~/.nvm/nvm.sh
# nvm use
# npm install
# npx prettier --write "./site/content/**/*.md" --print-width 80 --prose-wrap always

mdformat "./site/content/"