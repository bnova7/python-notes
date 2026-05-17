from notes.db import create_table

MAX_TITLE_LENGTH = 255
MAX_CONTENT_LENGTH = 1000

def add_note(title, content, cursor, connection):
    if not title.strip() or not content.strip():
        return False
    if len(title) > MAX_TITLE_LENGTH or len(content) > MAX_CONTENT_LENGTH:
        return False
    create_table()
    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    connection.commit()
    return True