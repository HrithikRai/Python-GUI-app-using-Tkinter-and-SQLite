import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("create table if not exists book(id integer PRIMARY KEY,title text ,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)",(title,author,year,isbn))  #NULL specifies the auto-increment value which is ID
    conn.commit()
    conn.close()
 
def view():             # Outputs records in tuples inside a list
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    rows= cur.fetchall()
    conn.close()
    return rows
    
def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book where title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows= cur.fetchall()
    conn.close()
    return rows

def delete(id):       # Here we need to grab a selection from the listbox
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?",(id,))  
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))  
    conn.commit()
    conn.close()

connect()
