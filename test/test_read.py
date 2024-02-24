import sqlite3
def read():
    conn = sqlite3.connect("database/test_musicdatabase.db")
    c = conn.cursor()

    c.execute("SELECT * FROM tracks")

    rows = c.fetchall

    for k in rows:
        print(k)

    conn.close()

print("Starting")
read()
print("Table is read")