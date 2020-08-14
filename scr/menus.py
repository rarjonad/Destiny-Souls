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
        modifiers.update({i: mod})
    return modifiers


def calculate_skill_value(skill, modifier):
    print(skill)
    skill['value'] = skill['points'] + modifier


def stat_assign():
    max_points = 72
    points_left = max_points
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
            print(i + ": " + str(main_stats[i]) + " | Modifier: " + str(stat_modifiers[i]))
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
    return main_stats, stat_modifiers


def skill_assign(stat_modifiers):
    # SKILL BLOCK
    print("\nSkills block\n")
    with open('data/player_skills.json') as skills_file:
        skill_list = json.load(skills_file)
    skill_count = 0
    for i in skill_list['skills']:  # Add point field to every skill for assigned points
        new_field = {'points': 0, 'value': stat_modifiers[i['stat']]}
        skill_list['skills'][skill_count].update(new_field)
        skill_count += 1
    skill_check = 0
    skill_points_max = 10 + stat_modifiers["INT"]
    skill_points_left = skill_points_max
    while skill_check == 0:  # Skill point assign loop
        count = 0
        print('Limit points: ' + str(skill_points_max) + ' Current left: ' + str(skill_points_left))
        print('\tSkill - Stat - Value - Points - Stat Modifier')
        print()
        for i in skill_list['skills']:
            print(str(count) + ') ' + i['id'] + ' - ' + i['stat'] + ' - ' + str(i['value']) + ' - ' + str(i['points']) + ' - ' + str(stat_modifiers[i['stat']]))
            count += 1
        print()
        chosen_skill = input("Choose Skill by number (empty to finish): ")
        if chosen_skill == '':
            if skill_points_left < 0:
                print('Over point limit. Reassign your skills')
                input('>...')
            elif skill_points_left > 0:
                print('Below point limit')
                skill_exit = input('Finish skill assign? [y/n] ')
                if skill_exit.lower() == "y":
                    skill_check = 1
            else:
                skill_check = 1
        else:
            try:
                chosen_skill = int(chosen_skill)
            except ValueError:
                pass
            else:
                try:
                    skill_list['skills'][chosen_skill]
                except IndexError:
                    print("Skill NOT found")
                else:
                    print("Skill found")
                    skill_found = skill_list['skills'][chosen_skill]
                    try:
                        skill_points_assign = int(input("How many points to assign? "))
                    except ValueError:
                        pass
                    else:
                        skill_found['points'] = skill_points_assign
                        skill_found = calculate_skill_value(skill_found, stat_modifiers[skill_found['stat']])
                        skill_points_left -= skill_points_assign
    return skill_list


def chargen():
    name = input("Choose name: ")
    main_stats, stat_modifiers = stat_assign()  # Get main stats
    skill_list = skill_assign(stat_modifiers)  # Get Skills
    level = 1
    exp = 0
    hp = 10 + stat_modifiers["CON"]
    mp = 20 + stat_modifiers["INT"]
    print("hp: " + str(hp))
    print("mp: " + str(mp))
    player = pl.Player(name, hp, mp, level, exp, main_stats, stat_modifiers, skill_list)
    print("\nPlayer data\n")
    print(player)
    print(dir(player))
    print(player.stats)
    print(player.stats_modifiers)
    for i in player.skills:
        print(player.skills[i])
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
