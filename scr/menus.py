import player as pl


def chargen():
    name = input("Choose name: ")
    level = 1
    max_points = 72
    exp = 0
    stat_check = 0
    spent_points = 0
    main_stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
    # Loop asignar stats
    while stat_check == 0:
        print("Maximum Points to spend: " + str(max_points))
        spent_points = 0
        for i in main_stats:
            main_stats[i] = int(input(i+" Choose amount:"))
            spent_points += main_stats[i]
            print("leftover points: " + str(max_points-spent_points))

        print(main_stats)
        if max_points >= spent_points:
            print("spent points: " + str(spent_points))
            print("stat points: " + str(max_points))
            print("leftover points: " + str(max_points-spent_points))
            stat_check = 1

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
