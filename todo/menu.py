import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)



MENU_DICT ={
    1: "create",
    2: "view",
    3: "complete",
    4: "uncomplete",
    5: "edit",
    6: "delete",
    7: "exit",
}


def menu() -> str:
    print(Fore.MAGENTA + "="*36)
    print(Fore.GREEN + "              OPTIONS")
    print(Fore.MAGENTA + "="*36)

    print(Fore.WHITE + " [1] " +  Fore.LIGHTCYAN_EX + "CREATE TASK")
    print(Fore.WHITE + " [2] " +  Fore.LIGHTCYAN_EX + "VIEW TASK")
    print(Fore.WHITE + " [3] " +  Fore.LIGHTCYAN_EX + "COMPLETE TASK")
    print(Fore.WHITE + " [4] " +  Fore.LIGHTCYAN_EX + "UNCOMPLETE TASK")
    print(Fore.WHITE + " [5] " +  Fore.LIGHTCYAN_EX + "EDIT TASK")
    print(Fore.WHITE + " [6] " +  Fore.LIGHTCYAN_EX + "DELETE TASK") 
    print(Fore.WHITE + " [7] " +  Fore.LIGHTCYAN_EX + "EXIT") 

