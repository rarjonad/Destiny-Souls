import chargen as chrgn


def new_game():
    print("New game started")
    player = chrgn.chargen()
    print("Character created")


def load_game():
    pass


def options():
    pass


main_switcher = {
    1: new_game,
    2: load_game,
    3: options,
    4: exit,
}


def main_menu():
    menu1 = 1
    while menu1 == 1:
        print("\t\t 1- New Game")
        print("\t\t 2- Load Game")
        print("\t\t 3- Options")
        print("\t\t 4- Exit")
        print()
        try:
            chosen_option = int(input("Choose: "))
        except ValueError:
            pass
        else:
            exec_menu = main_switcher.get(chosen_option, 0)
            if exec_menu != 0:
                exec_menu()
