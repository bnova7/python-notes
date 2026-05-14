from db import create_table



def add_note(title, content, cursor, connection):
    create_table()
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    connection.commit()