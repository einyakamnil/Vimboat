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
        self.n_articles = self._count_articles()
        self.n_unread = self._count_unread()
        return conn.close()

    def _count_articles(self):
        """Counts the total number of articles using a SQL query and returns it.
        Used for the n_articles attribute.
        """
        conn = apsw.Connection(
            DB,
            flags=apsw.SQLITE_OPEN_READONLY
        )
        query = (
            "SELECT COUNT(*) FROM rss_item "
            f"WHERE feedurl = '{self.rssurl}'"
        )
        n_articles = next(conn.execute(query))[0]
        conn.close()
        return n_articles

    def _count_unread(self):
        """Counts the number of unread articles using a SQL query and returns it.
        Used for the n_unread attribute.
        """
        conn = apsw.Connection(
            DB,
            flags=apsw.SQLITE_OPEN_READONLY
        )
        query = (
            "SELECT COUNT(*) FROM rss_item "
            f"WHERE feedurl = '{self.rssurl}' "
            "AND unread = 1 "
        )
        n_unread = next(conn.execute(query))[0]
        conn.close()
        return n_unread


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
    def feedform(feed):
        """Formats the feed to show unread to total articles ration and the
        title of the feed.
        """
        return f"({str(feed.n_unread)}/{str(feed.n_articles)})    {feed.title}"

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
    vimboat.feedkeys("dG")
    boatbuf = next(iter(vimboat.buffers))
    boatbuf.append([feedform(f) for f in feeds])
    vimboat.close()
