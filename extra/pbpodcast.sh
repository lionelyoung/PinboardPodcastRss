#!/usr/bin/env bash
# mkvirtualenv PinboardPodcastRss
# pip install -r pip-requirements

PBPCDIR=${PBPCDIR:-$HOME/Projects/PinboardPodcastRss/}
REMOTE=${REMOTE:-myserver:/srv/www/mysite/}
LOCAL=${LOCAL:-$PBPCDIR/pinduff.rss}

cd $PBPCDIR || exit 1

$HOME/.virtualenvs/PinboardPodcastRss/bin/python pbpodcast.py && rsync -avzue ssh "$LOCAL" "$REMOTE"
