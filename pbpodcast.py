#!/usr/bin/env python
from feedgen.feed import FeedGenerator
from pinboard import Pinboard
from config import api_token, limit_tags, output
from pytz import utc

if __name__ == "__main__":
    # create the feed
    fg = FeedGenerator()
    fg.id('pbpodcast123')
    fg.title('Pinboard RSS')
    fg.author({'name': 'John Smith', 'email': 'john@example.com'})
    fg.link(href='http://example.com', rel='alternate')
    fg.logo('http://example.com/logo.jpg')
    fg.subtitle('This is a cool feed!')
    fg.link(href='http://example.com/pinduff.rss', rel='self')
    fg.language('en')

    # podcast
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Technology', 'Podcasting')

    # get recent posts from pinboard
    pb = Pinboard(api_token)
    bookmarks = pb.posts.recent(tag=limit_tags)

    # add feed entries only if they are mp3s
    for bm in bookmarks['posts']:
        if 'mp3' in bm.url:
            fe = fg.add_entry()
            fe.id(bm.url)
            fe.pubdate(utc.localize(bm.time))
            fe.title(bm.description)
            fe.description(bm.extended)
            fe.enclosure(bm.url, 0, "audio/mpeg")

    # generate feed
    fg.rss_file(output)
