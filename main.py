from todo.menu import menu, user_choice, MENU_DICT


def main():
    while True:
        menu()
        choice = user_choice(MENU_DICT, "Choice: ")
        break





if __name__ == "__main__":
    main()