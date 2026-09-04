from todo.task import Task
from todo.task_manager import TaskManager
from todo.storage import JSONStorage


task1 = Task("101", "Morning Run", "Run 5km in 18 minutes in the morning.", "High", "26-09-2026")
task2 = Task("102", "Work on Project", "Finish CRUD operations in Todo project.", "Medium", "26-09-2026")
task3 = Task("103", "Learn OOPs", "Learn property decorators", "Low", "27-09-2026")


storage = JSONStorage("storage/tasks.json")
manager = TaskManager(storage = storage)

tasks = [task1, task2, task3]
for task in tasks:
    manager.add_task(task)

manager.update_task("101", title= "Morning 5KM drill")

manager.save()
print(storage.load())