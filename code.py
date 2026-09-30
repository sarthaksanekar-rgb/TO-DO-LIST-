
# Python To-Do List
# Terminal-based task manager

tasks = []


def show_tasks():
    print("\n========== MY TO-DO LIST ==========")

    if not tasks:
        print("Your task list is empty.")
        return

    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. [{status}] {task['name']}")


def add_task():
    print("\n--- ADD TASK ---")
    name = input("Enter task name: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    tasks.append({"name": name, "done": False})
    print("Task added successfully!")


def get_task_number():
    if not tasks:
        print("No tasks available.")
        return None

    show_tasks()

    try:
        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            return number - 1
        print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

    return None


def complete_task():
    print("\n--- COMPLETE TASK ---")
    index = get_task_number()

    if index is None:
        return

    if tasks[index]["done"]:
        print("This task is already completed.")
    else:
        tasks[index]["done"] = True
        print("Task marked as completed!")


def edit_task():
    print("\n--- EDIT TASK ---")
    index = get_task_number()

    if index is None:
        return

    new_name = input("Enter updated task name: ").strip()

    if new_name:
        tasks[index]["name"] = new_name
        print("Task updated successfully!")
    else:
        print("Task name cannot be empty.")


def delete_task():
    print("\n--- DELETE TASK ---")
    index = get_task_number()

    if index is None:
        return

    confirm = input("Delete this task? (y/n): ").strip().lower()

    if confirm == "y":
        removed = tasks.pop(index)
        print(f"Deleted task: {removed['name']}")
    else:
        print("Deletion cancelled.")


def show_pending():
    print("\n--- PENDING TASKS ---")
    pending = [
        task for task in tasks if not task["done"]
    ]

    if not pending:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending, 1):
        print(f"{i}. {task['name']}")


def show_menu():
    print("\n" + "=" * 35)
    print("          TO-DO LIST")
    print("=" * 35)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. View pending tasks")
    print("7. Exit")
    print("=" * 35)


def main():
    print("Welcome to your To-Do List!")

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            show_pending()
        elif choice == "7":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
    