import apsw
from bs4 import BeautifulSoup
from pynvim import attach
import re
import requests

DB = "../../share/vimboat/cache.db"

class Feed:
    """Feed object
    """
    def __init__(self, rssurl):
        conn = apsw.Connection(
            DB,
            flags=apsw.SQLITE_OPEN_READONLY
        )
        db_query = next(conn.execute(
            f"SELECT url,title,lastmodified,etag FROM rss_feed WHERE rssurl = '{rssurl}'"
        ))
        self.rssurl = rssurl
        self.source_url = db_query[0]
        self.title  = db_query[1]
        self.last_mod  = db_query[2]
        self.etag  = db_query[3]
        pass


class Article:
    """Article object
    """
    def __init__(self, url):
#        self.author
#        self.guid
#        self.title
#        self.feedurl
#        self.pubDate
#        self.content
#        self.unread
#        self.deleted
        pass


if __name__ == '__main__':
    sk = "/tmp/nvim.socket"
    rssurls = [
        "https://www.archlinux.org/feeds/news/",
        "https://suckless.org/atom.xml",
        "https://lukesmith.xyz/rss.xml",
        "https://notrelated.xyz/rss",
        "https://www.pathofexile.com/news/rss",
        "https://fractalsoftworks.com/feed/"
    ]
    feeds = [Feed(r) for r in rssurls]
    vimboat = attach('socket', path=sk)
    boatbuf = next(iter(vimboat.buffers))
    boatbuf.append(rssurls)
    vimboat.close()
