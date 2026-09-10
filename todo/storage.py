import json
import csv
from pathlib import Path
from todo.task import Task

class JSONStorage:

    # We create a constructor to create filepath
    def __init__(self, filepath):
        self.filepath = Path(filepath)

    # This file saves data to json
    def save(self, tasks):
        data = [task.to_dict() for task in tasks]
        with open (self.filepath, "w") as f:
            json.dump(data, f, indent=4)
    # This file loads data from json file
    def load(self):
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []

        return [Task.from_dict(i) for i in data]


# This is another class for the purpose of CSV storage
class CSVStorage:

    # Here it takes the same filepath and creates title for them
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.fieldnames = ["task_id", "title", "description", "priority", "status", "due_date"]

    # This saves tasks to csv
    def save(self, tasks):
        with open(self.filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    # This loads tasks from csv      
    def load(self):
        try:
            with open(self.filepath, "r", newline="") as f:
                reader = csv.DictReader(f)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []        