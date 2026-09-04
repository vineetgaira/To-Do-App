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


