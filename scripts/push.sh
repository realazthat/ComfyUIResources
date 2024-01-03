# https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
set -e -x -v -u -o pipefail

GITHUB_PAGES_BRANCH=gh-pages
OUTPUTDIR=site/output

ghp-import -b $GITHUB_PAGES_BRANCH -m "Generate Pelican site" "$OUTPUTDIR"
git push origin $(GITHUB_PAGES_BRANCH)
