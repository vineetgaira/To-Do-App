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

    def __init__(self, task_id, title, description, priority, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "incomplete"
        self.due_date = due_date

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

    def update_task(self, task_id, title = None, description = None, priority = None, due_date = None):
        pass

    def complete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print(f"No task found with Task ID: {task_id}.")
        task.status = "complete"

    def list_tasks(self):
        for task in self.tasks:
            task.get_task()


task1 = Task("101", "Morning Run", "Run 5km in 18 minutes in the morning.", "High", "26-09-2026")
task2 = Task("102", "Work on Project", "Finish CRUD operations in Todo project.", "Medium", "26-09-2026")
task2 = Task("103", "Learn OOPs", "Learn property decorators", "Low", "27-09-2026")
manager = TaskManager()

manager.add_task(task1)
manager.add_task(task2)
manager.list_tasks()