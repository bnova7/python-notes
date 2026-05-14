
from db import c 

def get_all_notes():
    c.execute('SELECT * FROM notes')
    return c.fetchall()

def get_note_by_id(note_id):
    c.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
    return c.fetchone()

