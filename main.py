import rich
from delete import delete_note
from write import add_note
from rich.console import Console
import view 
from db import c, conn



def main():
    console = Console()
    try:
        while True:
            console.print("\nMenu:", style="bold yellow")
            console.print("1. Add Note", style="bold blue")
            console.print("2. View All Notes", style="bold blue")
            console.print("3. View Note by ID", style="bold blue")
            console.print("4. Delete Note", style="bold blue")
            console.print("0. Exit", style="bold blue")

            try:
                choice = int(input("Enter a number (0 to exit): "))
                if choice == 1:
                    title = input("Enter note title: ")
                    content = input("Enter note content: ")
                    if add_note(title,content,c,conn):
                        console.print("Note added successfully.", style="bold blue")
                    else:
                        console.print("Cannot add empty note", style="bold red")
                elif choice == 2:
                    view.display_all_notes()
                elif choice == 3:
                    view.list_note_titles()
                    note_id = int(input("Enter note ID: "))
                    view.display_note_by_id(note_id)
                elif choice == 4:
                    view.list_note_titles()
                    note_id = int(input("Enter note ID to delete: "))
                    delete_note(note_id, c, conn)
                elif choice == 0:
                    exit(0)
                else:
                    console.print("Invalid choice, try again.", style="bold red")
            except ValueError:
                console.print("[red]Invalid value. try again. [/red]")
                
    except KeyboardInterrupt:
        print("Goodbye.")

if __name__ == "__main__":
    main()