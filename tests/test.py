import unittest 
import sqlite3

from delete import delete_note
from write import add_note
from view import get_all_notes, get_note_by_id


class TestNotes(unittest.TestCase):
    def setUp(self):
       self.conn =  sqlite3.connect(":memory:")
       self.c = self.conn.cursor()
       self.c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL)''')
    def test_add_note(self):
        add_note("title", "content", self.c, self.conn)
        result = get_all_notes(self.c)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "title")
        self.assertEqual(result[0][2], "content")

    def test_get_note_by_id(self):
        add_note("title", "content", self.c, self.conn)
        result = get_note_by_id(1, self.c)
        self.assertEqual(result[1], "title")
        self.assertEqual(result[2],"content")


    def test_delete(self):
        add_note("title", "content", self.c, self.conn)
        delete_note(1, self.c, self.conn)
        result = get_all_notes(self.c)
        self.assertEqual(len(result), 0)
        
    def test_get_note_by_id_is_not_found(self):
        result = get_note_by_id(999, self.c)
        self.assertIsNone(result)
        

    
