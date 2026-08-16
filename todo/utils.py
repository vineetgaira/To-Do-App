import os
from colorama import Fore

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_error(error):
    print(Fore.RED + error)