import json
import csv
from pathlib import Path
from todo.task import Task

class JSONStorage:

    def __init__(self, filepath):
        self.filepath = Path(filepath)

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

class CSVStorage:

    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.fieldnames = ["task_id", "title", "description", "priority", "status", "due_date"]


    def save(self, tasks):
        with open(self.filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
    def load(self):
        try:
            with open(self.filepath, "r", newline="") as f:
                reader = csv.DictReader(f)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []        