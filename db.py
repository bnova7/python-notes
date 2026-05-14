import sqlite3

testconn = sqlite3.connect(":memory:")
testc=testconn.cursor

conn = sqlite3.connect('notes.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  content TEXT NOT NULL)''')
    conn.commit()