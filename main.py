import rich
from delete import delete_note
from write import add_note
from rich.console import Console
from view import get_all_notes, get_note_by_id, list_note_titles, display_all_notes, display_note_by_id



def main():
    console = Console()
    console.print("Hello, World!", style="bold green")
    try:
        while True:
            console.print("\nMenu:", style="bold yellow")
            console.print("1. Add Note", style="bold blue")
            console.print("2. View All Notes", style="bold blue")
            console.print("3. View Note by ID", style="bold blue")
            console.print("4. Delete Note", style="bold blue")
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
                list_note_titles()
                note_id = int(input("Enter note ID: "))
                display_note_by_id(note_id)
            elif choice == 4:
                list_note_titles()
                note_id = int(input("Enter note ID to delete: "))
                delete_note(note_id)
            elif choice == 0:
                exit(0)
            else:
                console.print("Invalid choice, try again.", style="bold red")
    except KeyboardInterrupt:
        print("Goodbye.")

if __name__ == "__main__":
    main()