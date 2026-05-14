
from db import c 
from rich.console import Console 

def get_all_notes(cursor):
    cursor.execute('SELECT * FROM notes')
    return cursor.fetchall()

def get_note_by_id(note_id, cursor):
    cursor.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
    return cursor.fetchone()

def list_note_titles():
    notes = get_all_notes(c)
    for note in notes:
        print(f"[{note[0]}: {note[1]}]")

def display_note_by_id(note_id):
    console = Console()
    note = get_note_by_id(note_id, c)
    if note:
        console.print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}", style="bold magenta")
    else:
        console.print("Note not found.", style="bold red")


def display_all_notes():
    console = Console()
    notes = get_all_notes(c)
    for note in notes:
        console.print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}", style="bold cyan")
