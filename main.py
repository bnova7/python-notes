import rich
from delete import delete_note
from write import add_note
from rich.console import Console
from view import get_all_notes, get_note_by_id

def display_note_by_id(note_id):
    console = Console()
    note = get_note_by_id(note_id)
    if note:
        console.print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}", style="bold magenta")
    else:
        console.print("Note not found.", style="bold red")


def display_all_notes():
    console = Console()
    notes = get_all_notes()
    for note in notes:
        console.print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}", style="bold cyan")

def main():
    console = Console()
    console.print("Hello, World!", style="bold green")
    while True:
        console.print("\nMenu:", style="bold yellow")
        console.print("1. Add Note", style="bold blue")
        console.print("2. View All Notes", style="bold blue")
        console.print("3. View Note by ID", style="bold blue")
        console.print("0. Exit", style="bold blue")

        choice = int(input("Enter a number (0 to exit): "))
        if choice == 1:
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)
            console.print("Note added successfully.", style="bold blue")
        elif choice == 2:
            display_all_notes()
        elif choice == 3:
            note_id = int(input("Enter note ID: "))
            display_note_by_id(note_id)
        elif choice == 4:
            note_id = int(input("Enter note ID to delete: "))
            delete_note(note_id)
        elif choice == 0:
            exit(0)
        else:
            console.print("Invalid choice, try again.", style="bold red")

if __name__ == "__main__":
    main()