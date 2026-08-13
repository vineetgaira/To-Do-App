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
    

while True:
    task_id = random.randint(1,1001)
    title = input(Fore.BLUE + "Enter title of the task: ")
    description = input(Fore.BLUE + "Enter description of the task: ")
    task = Task(task_id, title, description)
    task_id+=1
    print(Fore.LIGHTCYAN_EX + f"{task}")
    ask_exit = input(Fore.BLUE + "Do you wanna add one more task? y/n: ").strip().lower()
    if ask_exit == "y":
        continue
    elif ask_exit == "n":
        break
    else:
        print(Fore.RED + "Please enter 'y/n.")
  