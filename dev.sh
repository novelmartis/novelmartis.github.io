#!/usr/bin/env bash
set -e

docker run --rm -it \
  --platform linux/amd64 \
  -p 4000:4000 -p 35729:35729 \
  -v "$PWD:/srv/jekyll" \
  -e BUNDLE_GEMFILE=/srv/jekyll/Gemfile.docker \
  -e BUNDLE_PATH=/srv/jekyll/.bundle-docker \
  jekyll/jekyll:4 \
  sh -lc "bundle config set path /srv/jekyll/.bundle-docker && bundle install && bundle exec jekyll serve --livereload --force_polling --host 0.0.0.0 --destination /srv/jekyll/_site --trace"
