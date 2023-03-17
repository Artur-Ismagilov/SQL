import sqlite3 as sq

cars = [('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)]

con = None

try:

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

    cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    con.commit()

except sq.Error as e:
    if con: con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con: con.close()