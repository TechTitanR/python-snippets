# Simple Password Saver 
import json
import os

DATA_FILE = "passwords.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def encrypt(text):
    return ''.join(chr(ord(c) + 3) for c in text)  # Caesar cipher

def decrypt(text):
    return ''.join(chr(ord(c) - 3) for c in text)

def add_password():
    site = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")
    data = load_data()
    data[site] = {"username": username, "password": encrypt(password)}
    save_data(data)
    print("✅ Password saved.")

def view_passwords():
    data = load_data()
    if not data:
        print("No credentials found.")
        return
    for site, info in data.items():
        print(f"\n🌐 {site}")
        print(f"👤 {info['username']}")
        print(f"🔑 {decrypt(info['password'])}")

def search_password():
    data = load_data()
    site = input("Enter website to search: ")
    if site in data:
        print(f"\n🌐 {site}")
        print(f"👤 {data[site]['username']}")
        print(f"🔑 {decrypt(data[site]['password'])}")
    else:
        print("❌ No credentials found for that website.")

def delete_password():
    data = load_data()
    site = input("Enter website to delete: ")
    if site in data:
        del data[site]
        save_data(data)
        print("🗑️ Credentials deleted.")
    else:
        print("❌ Website not found.")

def main():
    while True:
        print("\n--- PASSWORD SAVER ---")
        print("1. Add password")
        print("2. View all passwords")
        print("3. Search password")
        print("4. Delete password")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("👋 Exiting Password Saver.")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == "__main__":
    main()
