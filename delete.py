from db import c, conn

def delete_note(note_id):
    c.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
