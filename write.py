from db import create_table



def add_note(title, content, cursor, connection):
    if not title.strip() or  not content.strip():
        return False
    create_table()
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    connection.commit()
    return True