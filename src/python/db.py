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

#for i in list(item_cols):
#    print(i)
feeds = conn.execute(
    "SELECT title,etag FROM rss_feed WHERE LENGTH(etag) > 0"
)

for f in list(feeds):
    print(f)
