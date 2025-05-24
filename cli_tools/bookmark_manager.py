# Bookmark Manager
import json
import os

BOOKMARK_FILE = "bookmarks.json"

def load_bookmarks():
    if os.path.exists(BOOKMARK_FILE):
        with open(BOOKMARK_FILE, "r") as f:
            return json.load(f)
    return []

def save_bookmarks(bookmarks):
    with open(BOOKMARK_FILE, "w") as f:
        json.dump(bookmarks, f, indent=2)

def add_bookmark():
    title = input("Enter bookmark title: ")
    url = input("Enter bookmark URL: ")

    bookmarks = load_bookmarks()

    new_bookmark = {
        "title": title,
        "url": url
    }

    bookmarks.append(new_bookmark)
    save_bookmarks(bookmarks)

    print(f"\n✅ Bookmark '{title}' saved successfully.")

def main():
    print("--- 📚 Bookmark Manager ---")

    while True:
        print("\nChoose an option:")
        print("1. Add Bookmark")
        print("2. Exit")

        choice = input("Enter choice (1-2): ").strip()

        if choice == "1":
            add_bookmark()
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
