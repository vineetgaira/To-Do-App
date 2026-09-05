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