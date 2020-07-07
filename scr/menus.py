import player as pl
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def chargen():
    name = input("Choose name: ")
    level = 1
    max_points = 72
    points_left = max_points
    exp = 0
    stat_check = 0
    main_stats = {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}
    # Loop asignar stats
    while stat_check == 0:
        clear()
        print("Character generation\t\t Points left to spend: " + str(points_left))
        print("Minimum value is 1, Maximum value is 18")
        print("")
        for i in main_stats:
            print(i + ": " + str(main_stats[i]) + " | Modifier: " + str(main_stats[i]//2-5))
        input_stat = input("Write stat or 'Done' for exit: ")
        input_stat = input_stat.upper()
        if input_stat == "DONE":
            if (points_left > 0):
                print("You still have " + str(points_left) + " points left")
                point_confirm = input("Finish stat asignment? [y/n] ")
                if point_confirm.lower() == "y":
                    stat_check = 1
            elif (points_left < 0):
                print("Spent points ("+str(points_left)+") lower than 0")
                input(">...")
            else:
                stat_check = 1
        else:
            chosen_stat = main_stats.get(input_stat, 0)
            if chosen_stat == 0:
                pass
            else:
                stat_increase = int(input("Choose points to assign: "))
                if (stat_increase <= 0) or (stat_increase > 18):
                    print("Value must be between 1 and 18")
                    input(">...")
                else:
                    main_stats[input_stat] = stat_increase
                    points_left = max_points - sum(main_stats.values())

    hp = 10 + main_stats["CON"]//2
    mp = 20 + main_stats["INT"]//2
    print("hp: " + str(hp))
    print("mp: " + str(mp))
    player = pl.Player(name, hp, mp, level, exp, main_stats)
    print(player)
    print(dir(player))
    print(player.stats)
    return player


def new_game():
    print("New game started")
    player = chargen()
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
        chosen_option = int(input("Choose: "))
        exec_func = main_switcher.get(chosen_option, 0)
        if exec_func != 0:
            return exec_func()
