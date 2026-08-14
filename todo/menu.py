import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


def menu() -> str:
    print(Fore.MAGENTA + "="*36)
    print(Fore.GREEN + "              OPTIONS")
    print(Fore.MAGENTA + "="*36)

# Create task  
# View tasks
# Complete task
# Uncomplete task
# Edit task
# Delete task

menu()