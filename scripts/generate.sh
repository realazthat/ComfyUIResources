# https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
set -e -x -v -u -o pipefail


PATH_TO_SITE=$PWD/site
PATH_TO_THEME=$PWD/monospace-andrewboring


bash scripts/format.sh

cd "$PATH_TO_SITE"
pelican \
  -s publishconf.py \
  -t "$PATH_TO_THEME" \
  "$PATH_TO_SITE" 


# pelican --listen $PATH_TO_SITE

