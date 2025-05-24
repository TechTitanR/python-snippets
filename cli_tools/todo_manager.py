# To-Do List Manager
import json
import os

TODO_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(TODO_FILE, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        self.save_tasks()
        print("✅ Task added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks):
            status = "✅" if task["completed"] else "❌"
            print(f"{i + 1}. {task['description']} [{status}]")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("✅ Task marked as completed.")
        else:
            print("⚠️ Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑️ Task '{removed['description']}' deleted.")
        else:
            print("⚠️ Invalid task number.")

def main():
    manager = TaskManager()

    while True:
        print("\n--- TO-DO MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            desc = input("Enter task description: ")
            manager.add_task(desc)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            i = int(input("Enter task number to mark as done: ")) - 1
            manager.mark_done(i)
        elif choice == "4":
            manager.list_tasks()
            i = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(i)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
