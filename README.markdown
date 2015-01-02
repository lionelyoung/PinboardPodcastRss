# Config

The config.py contains your Pinbaord API token, so it can grab the recent
posts.  Use `limit_tags` to filter certain tags

1. Visit https://pinboard.in/settings/password to get your API token
2. Create file `config.py` (see `config.py.example`) with `api_token` and `limit_tags`

	api_token = "jsmith:9ABC8DEF7GHI6JKL5MNO"
	limit_tags = ["mp3"]
	output = "pinduff.rss"

# Usage

Dependencies are feedgen and pinboard.  See pip-requirements.txt

1. To install dependencies: pip install -r pip-requirements.txt
2. Run: python pbpodcast.py

Now upload your rss file (default is `pinduff.rss`) where you want it.  For example:

	rsync -avzue ssh pinduff.rss myserver:/srv/www/mysite/
