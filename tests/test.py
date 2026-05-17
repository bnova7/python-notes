import unittest 
import sqlite3

from notes.delete import delete_note
from notes.write import add_note
from notes.view import get_all_notes, get_note_by_id


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

    def test_add_note_with_empty_content(self):
        result = add_note("title", "", self.c, self.conn)
        self.assertFalse(result)

    def test_add_note_with_whitespace_title(self):
        result = add_note("   ", "content", self.c, self.conn)
        self.assertFalse(result)

    def test_get_all_notes_with_empty_database(self):
        result = get_all_notes(self.c)
        self.assertEqual(len(result), 0)

    def test_delete_non_existent_note(self):
        result = delete_note(999, self.c, self.conn)
        self.assertFalse(result)

    def test_display_all_notes_with_multiple_entries(self):
        add_note("title1", "content1", self.c, self.conn)
        add_note("title2", "content2", self.c, self.conn)
        result = get_all_notes(self.c)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][1], "title1")
        self.assertEqual(result[0][2], "content1")
        self.assertEqual(result[1][1], "title2")
        self.assertEqual(result[1][2], "content2")

    def test_display_note_by_id(self):
        add_note("title", "content", self.c, self.conn)
        result = get_note_by_id(1, self.c)
        self.assertEqual(result[1], "title")
        self.assertEqual(result[2], "content")

    def test_display_note_by_id_with_non_existent_id(self):
        result = get_note_by_id(999, self.c)
        self.assertIsNone(result)

    def display_note_by_id_with_invalid_id(self):
        result = get_note_by_id("invalid", self.c)
        self.assertIsNone(result)
    
    def test_delete_note_with_non_existent_id(self):
        result = delete_note(999, self.c, self.conn)
        self.assertFalse(result)

    def test_delete_note_with_invalid_id(self):
        result = delete_note("invalid", self.c, self.conn)
        self.assertFalse(result)

    def test_add_note_with_long_title(self):
        long_title = "a" * 256
        result = add_note(long_title, "content", self.c, self.conn)
        self.assertFalse(result)
        
    
    def test_display_note_by_id_with_special_chars(self):
        result = get_note_by_id("!@#$%^&*()", self.c)
        self.assertIsNone(result)


if __name__ == '__main__':    unittest.main()

    
    
