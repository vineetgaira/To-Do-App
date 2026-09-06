from todo.task import Task
from todo.task_manager import TaskManager
from todo.storage import JSONStorage, CSVStorage

def menu():

    print("=" * 46) 
    print("             MENU")
    print("=" * 46) 

    print(" [1] ", "Add Task")
    print(" [2] ", "Update Task")
    print(" [3] ", "Remove Task")
    print(" [4] ", "See Tasks")

def get_choice():
    valid_choices = {1, 2, 3, 4}
    while True:
        try:
            choice = int(input("Choice: "))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print('Please enter a valid choice.')


        
        
        

    