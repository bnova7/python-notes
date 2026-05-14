from db import conn, c, create_table



def add_note(title, content):
    create_table()
    c.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    conn.commit()