import sqlite3

def connect():
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS address (id INTEGER PRIMARY KEY, website text)")
    conn.commit()
    conn.close()
connect()

def insert(adrs):
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO address VALUES(NULL,?)",(adrs,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(adrs):
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address WHERE website=?",(adrs,))


insert("www.facebook.com")
print(view())
