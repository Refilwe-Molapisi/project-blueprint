#!/bin/sh
# Vercel build step: assembles the deployable web root into dist/.
#
# The repository root also holds repository-only files — docs/ (internal
# documentation), generator/ (site source), README.md and this script. Those
# are deliberately NOT deployed; only the website itself goes into dist/.
# See docs/deployment.md. To publish the docs too, add a docs/ copy below.
set -eu

rm -rf dist
mkdir -p dist

cp ./*.html dist/          # all pages, including index.html and 404.html
cp ./robots.txt ./sitemap.xml dist/
cp -R ./assets dist/       # style.css, site.js, favicon.svg
