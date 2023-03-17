import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT not null,
        sex integer default 1,
        old integer,
        score integer
        ) 
    """)