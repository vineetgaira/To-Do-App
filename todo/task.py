import colorama
import random
from colorama import Fore, Style
colorama.init(autoreset=True)
class Task:

    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def uncomplete(self):
        self.complete = False

    def update(self, title, description):
        self.title = title
        self.description = description
    
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.task_id} - {self.title} - {self.description}"
    


