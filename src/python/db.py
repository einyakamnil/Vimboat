import apsw


conn = apsw.Connection(
    "../../share/vimboat/cache.db",
    flags=apsw.SQLITE_OPEN_READONLY
)
item_cols = conn.execute(
    "PRAGMA table_info('rss_item')"
)
feed_cols = conn.execute(
    "PRAGMA table_info('rss_feed')"
)

#for i in list(feed_cols):
#    print(i)
#
#for i in list(item_cols):
#    print(i)
#
#feeds = conn.execute(
#    "SELECT title,rssurl FROM rss_feed"
#)

kammer = next(
    conn.execute(
        "SELECT rssurl FROM rss_feed WHERE title = 'Kammerbild'"
    )
)[0]

items = list(
    conn.execute(
        f"SELECT Count(*) FROM rss_item WHERE feedurl = '{kammer}' AND unread = 1"
    )
)

print(len(items))
for i in items:
    print(i)
