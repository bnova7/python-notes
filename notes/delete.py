from notes.db import c, conn

def delete_note(note_id, cursor, connection):
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    connection.commit()
