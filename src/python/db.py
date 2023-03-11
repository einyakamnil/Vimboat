import apsw


conn = apsw.Connection(
#    "../../share/vimboat/cache.db",
    "/home/linkai/.local/share/newsboat/cache.db",
    flags=apsw.SQLITE_OPEN_READONLY
)
item_cols = conn.execute(
    "PRAGMA table_info('rss_item')"
)
feed_cols = conn.execute(
    "PRAGMA table_info('rss_feed')"
)
#print(next(feed_cols))

#for i in list(feed_cols):
#    print(i)

#for i in list(item_cols):
#    print(i)
#
#feeds = conn.execute(
#    "SELECT title,rssurl FROM rss_feed"
#)

kammer = next(
    conn.execute(
        "SELECT * FROM rss_feed WHERE title = 'Kammerbild'"
    )
)

feedurl = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCvigl2g67gl18hJgFex-3zg'
n_articles = next(
    conn.execute(
        f"SELECT COUNT(*) FROM rss_item WHERE feedurl = '{feedurl}'"
    )
)[0]
print(n_articles)

q = f"SELECT COUNT(*) FROM rss_item WHERE feedurl = '{feedurl}' AND unread = 1"
n_unread = next(
    conn.execute(
        q
    )
)[0]
print(n_unread)

#
#items = list(
#    conn.execute(
#        f"SELECT Count(*) FROM rss_item WHERE feedurl = '{kammer}' AND unread = 1"
#    )
#)
#
#print(len(items))
#for i in items:
#    print(i)
