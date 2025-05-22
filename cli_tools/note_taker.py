# note_taker.py

import os

NOTES_FILE = "cli_tools/notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("Note added!")

def read_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
    if not notes:
        print("No notes saved yet.")
    else:
        print("\nYour Notes:")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note.strip()}")

def edit_note():
    read_notes()
    try:
        index = int(input("\nEnter the number of the note to edit: ")) - 1
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
        if 0 <= index < len(notes):
            new_note = input("Enter the new content: ")
            notes[index] = new_note + "\n"
            with open(NOTES_FILE, "w") as f:
                f.writelines(notes)
            print("Note updated.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_note():
    read_notes()
    try:
        index = int(input("\nEnter the number of the note to delete: ")) - 1
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
        if 0 <= index < len(notes):
            deleted = notes.pop(index)
            with open(NOTES_FILE, "w") as f:
                f.writelines(notes)
            print(f"Deleted note: {deleted.strip()}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- Note Taker CLI ---")
        print("1. Add Note")
        print("2. Read Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
