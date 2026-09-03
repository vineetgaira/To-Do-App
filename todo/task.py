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

import json
import pathlib
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

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["task_id"], data["title"], data["description"], data["priority"], data["due_date"])
        task.status = data["status"]
        return task
class TaskManager:

    def __init__(self, storage = None):
        self.storage = storage
        self.tasks = self.storage.load() if self.storage else []

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
        task = self.find_task(task_id)

        if task is None:
            print(f"No task found with Task ID: {task_id}")
            return

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if priority is not None:
            task.priority = priority
        if due_date is not None:
            task.due_date = due_date

        print(f"Updated: {task.title}/{task.task_id}")
    def complete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print(f"No task found with Task ID: {task_id}.")
            return
        
        task.status = "complete"

    def save(self):
        if self.storage:
            self.storage.save(self.tasks)

class JSONStorage:

    def __init__(self, filepath ="tasks.json"):
        self.filepath = filepath

    def save(self, tasks):
        data = [task.to_dict() for task in tasks]
        with open (self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []

        return [Task.from_dict(i) for i in data]


task1 = Task("101", "Morning Run", "Run 5km in 18 minutes in the morning.", "High", "26-09-2026")
task2 = Task("102", "Work on Project", "Finish CRUD operations in Todo project.", "Medium", "26-09-2026")
task3 = Task("103", "Learn OOPs", "Learn property decorators", "Low", "27-09-2026")

storage = JSONStorage()
manager = TaskManager(storage = storage)

tasks = [task1, task2, task3]
for task in tasks:
    manager.add_task(task)

manager.update_task("101", title= "Morning 5KM drill")

manager.save()
print(storage.load())