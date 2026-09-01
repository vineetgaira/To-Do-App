"""
21. To-Do Application
    You were already working toward this, so this is a perfect project.
Build:
    Task
    TaskManager
    Storage
Eventually:
    Task
    ├── title
    ├── description
    ├── priority
    ├── status
    └── due_date
TaskManager:
    add_task()
    remove_task()
    update_task()
    complete_task()
    find_task()
    list_tasks()
Then introduce storage:
    JSONStorage
    FileStorage
Eventually you'll have:
    CLI
    ↓
    TaskManager
    ↓
    Storage
This is where everything you've learned starts coming together.
"""

class Task:

    total_tasks = 0

    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

        Task.total_tasks += 1

    def get_task(self):
        print(f"Task ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}\n")
class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)
        print(f"Added: {task.title}/{task.task_id}")

    def find_task(self, task_id):

        task = None

        for t in self.tasks:
            if t.task_id == task_id:
                task = t
                break

        return task


    def remove_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print(f"No task found with Task ID: {task_id}")
        else:
            self.tasks.remove(task)
            print(f"Removed: {task.title}/{task.task_id}")

task = Task("101", "Morning Run", "Run 5km in 18 minutes in the morning.")
manager = TaskManager()

manager.add_task(task)
task.get_task()
manager.remove_task("301")