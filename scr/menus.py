import player as pl
import os
import json


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def calculate_stat_modifiers(stats):
    modifiers = {}
    for i in stats:
        mod = stats[i] // 2 - 5
        modifiers.update({i + '_mod': mod})
    return modifiers


def chargen():
    name = input("Choose name: ")
    level = 1
    max_points = 72
    points_left = max_points
    exp = 0
    stat_check = 0
    main_stats = {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}
    # Loop stat assign
    while stat_check == 0:
        stat_modifiers = calculate_stat_modifiers(main_stats)
        clear()
        print("Character generation\t\t Points left to spend: " + str(points_left))
        print("Minimum value is 1, Maximum value is 18")
        print()
        for i in main_stats:
            print(i + ": " + str(main_stats[i]) + " | Modifier: " + str(stat_modifiers[i + '_mod']))
        input_stat = input("Write stat or 'Done' for exit: ")
        input_stat = input_stat.upper()
        if input_stat == "DONE":
            if (points_left > 0):
                print("You still have " + str(points_left) + " points left")
                point_confirm = input("Finish stat asignment? [y/n] ")
                if point_confirm.lower() == "y":
                    stat_check = 1
            elif (points_left < 0):
                print("Spent points (" + str(points_left) + ") lower than 0")
                input(">...")
            else:
                stat_check = 1
        else:
            chosen_stat = main_stats.get(input_stat, 0)
            if chosen_stat == 0:
                pass
            else:
                try:
                    stat_increase = int(input("Choose points to assign: "))
                except ValueError:
                    print("Write a number between 1 and 18")
                else:
                    if (stat_increase <= 0) or (stat_increase > 18):
                        print("Value must be between 1 and 18")
                        input(">...")
                    else:
                        main_stats[input_stat] = stat_increase
                        points_left = max_points - sum(main_stats.values())

    hp = 10 + stat_modifiers["CON_mod"]
    mp = 20 + stat_modifiers["INT_mod"]
    print("hp: " + str(hp))
    print("mp: " + str(mp))
    with open('data/player_skills.json') as skills_file:
        skill_list = json.load(skills_file)
    player = pl.Player(name, hp, mp, level, exp, main_stats, stat_modifiers, skill_list)
    print(player)
    print(dir(player))
    print(player.stats)
    print(player.stats_modifiers)
    print("\nSkills block\n")
    # Skills
    skill_check = 0
    skill_points_max = 10 + stat_modifiers["INT_mod"] * 2
    points = 2
    for i in player.skills:
        print(player.skills[i])

    # while skill_check == 0:
    #    for i in skills:
    #        print(i + ": \t" + str(skills[i]["points"]) + " (" + str(skills[i]["stat"]) + ")")
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
        try:
            chosen_option = int(input("Choose: "))
        except ValueError:
            pass
        else:
            exec_menu = main_switcher.get(chosen_option, 0)
            if exec_menu != 0:
                exec_menu()
