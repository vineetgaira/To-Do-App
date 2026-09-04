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