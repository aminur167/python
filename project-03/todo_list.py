# simple todo list manager - console app

tasks = []

def show_menu():
    print("\n--- Todo List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark complete")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print(f"Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "done" if t["done"] else "pending"
        print(f"  {i}. [{status}] {t['task']}")

def mark_complete():
    view_tasks()
    try:
        num = int(input("Task number to complete: "))
        tasks[num - 1]["done"] = True
        print("Marked as complete!")
    except (ValueError, IndexError):
        print("Invalid task number")

def delete_task():
    view_tasks()
    try:
        num = int(input("Task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid task number")

def main():
    while True:
        show_menu()
        choice = input("Choose (1-5): ")
        if choice == "1": add_task()
        elif choice == "2": view_tasks()
        elif choice == "3": mark_complete()
        elif choice == "4": delete_task()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
