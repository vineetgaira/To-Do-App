from todo.task import Task
from todo.task_manager import TaskManager
from todo.storage import JSONStorage, CSVStorage

def run_menu(manager):
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Remove Task")
        print("6. Save & Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task_id = input("Task ID: ")
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority: ")
            due_date = input("Due Date: ")
            manager.add_task(Task(task_id, title, description, priority, due_date))

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = input("Task ID to update: ")
            title = input("New title (leave blank to skip): ") or None
            manager.update_task(task_id, title=title)

        elif choice == "4":
            task_id = input("Task ID to complete: ")
            manager.complete_task(task_id)

        elif choice == "5":
            task_id = input("Task ID to remove: ")
            manager.remove_task(task_id)

        elif choice == "6":
            manager.save()
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    run_menu(TaskManager())
        

        

    