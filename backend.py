import sqlite3

def connect():
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS address (id INTEGER PRIMARY KEY, website text)")
    conn.commit()
    conn.close()


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
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM  address WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, adrs):
    conn=sqlite3.connect("addresses.db")
    cur=conn.cursor()
    cur.execute("UPDATE address SET website=? WHERE id=?",(adrs, id))
    conn.commit()
    conn.close()
