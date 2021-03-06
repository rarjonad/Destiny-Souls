import player as pl
import generic as gn
import json


def calculate_stat_modifiers(stats):
    modifiers = {}
    for i in stats:
        mod = stats[i] // 2 - 5
        modifiers.update({i: mod})
    return modifiers


def calculate_skill_value(skill, modifier):
    print(skill)
    skill['value'] = skill['points'] + modifier
    return skill


def menu_confirm(check_parameter):
    if check_parameter < 0:
        print('You have assigned more points than the maximum allowed.')
        input('>...')
        menu_check = 0
    elif check_parameter > 0:
        print('You still have points left to assign')
        skill_exit = input('Finish? [y/n] ')
        if skill_exit.lower() == "y":
            menu_check = 1
        else:
            menu_check = 0
    else:
        menu_check = 1
    return menu_check


def assign_stats(pre_stats):
    if pre_stats == 0:
        with open('data/player/player_main_stats.json') as stats_file:
            main_stats = json.load(stats_file)
    else:
        main_stats = pre_stats
    max_points = len(main_stats) * 10 + len(main_stats)
    points_left = max_points - sum(main_stats.values())
    stat_check = 0
    # Loop stat assign
    while stat_check == 0:
        stat_modifiers = calculate_stat_modifiers(main_stats)
        gn.clear()
        print("Character generation\t\t Points left to spend: " + str(points_left))
        print("Minimum value is 1, Maximum value is 18")
        print()
        for i in main_stats:
            print(i + ": " + str(main_stats[i]) + " | Modifier: " + str(stat_modifiers[i]))
        input_stat = input("Write stat or empty for exit: ")
        input_stat = input_stat.upper()
        if input_stat == "":
            stat_check = menu_confirm(points_left)
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


def assign_skills(pre_skill_list, stat_modifiers):
    print("\nSkills block\n")
    skill_list_assign = pre_skill_list
    skill_check = 0
    skill_points_max = 10 + stat_modifiers["INT"]
    skill_points_spent = 0
    for i in range(len(skill_list_assign['skills'])):  # Calculate spent points
        skill_points_spent += skill_list_assign['skills'][i]['points']
    print(str(skill_points_spent) + 'Points spent')
    skill_points_left = skill_points_max - skill_points_spent
    while skill_check == 0:  # Skill point assign loop
        count = 0
        print('Limit points: ' + str(skill_points_max) + ' Current left: ' + str(skill_points_left))
        print('\tSkill - Stat - Value - Points - Stat Modifier')
        print()
        for i in skill_list_assign['skills']:
            print(str(count) + ') ' + i['id'] + ' - ' + i['stat'] + ' - ' + str(i['value']) + ' - ' + str(i['points']) + ' - ' + str(stat_modifiers[i['stat']]))
            count += 1
        print()
        chosen_skill = input("Choose Skill by number (empty to finish): ")
        if chosen_skill == '':
            skill_check = menu_confirm(skill_points_left)
        else:
            try:
                chosen_skill = int(chosen_skill)
            except ValueError:
                pass
            else:
                try:
                    skill_list_assign['skills'][chosen_skill]
                except IndexError:
                    print("Skill NOT found")
                else:
                    print("Skill found")
                    skill_found = skill_list_assign['skills'][chosen_skill]
                    try:
                        skill_points_assign = int(input("How many points to assign? "))
                    except ValueError:
                        pass
                    else:
                        if skill_points_assign >= 0:
                            skill_points_difference = skill_points_assign - skill_found['points']
                            skill_found['points'] = skill_points_assign
                            skill_found = calculate_skill_value(skill_found, stat_modifiers[skill_found['stat']])
                            skill_points_left -= skill_points_difference
                        else:
                            print("No negative numbers")
                            input(">...")
    return skill_list_assign


def assign_abilities():
    pass


def assign_perks():
    pass


def finish_chargen():
    char_check = 1
    return char_check


def chargen():
    chargen_switcher = {
        1: assign_stats,
        2: assign_skills,
        3: assign_abilities,
        4: assign_perks,
        5: finish_chargen
    }
    chargen_check = 0
    name = input("Choose name: ")
    main_stats = 0  # def var so we can pass stats before player assigns them
    with open('data/player/player_skills.json') as skills_file:  # same as above with skills
        skill_list = json.load(skills_file)

    while chargen_check == 0:
        gn.clear()
        for k, v in chargen_switcher.items():
            text = str(v).split(' ')
            text[1] = text[1].replace('_', ' ')
            print(str(k) + ": " + text[1].capitalize())

        try:
            chosen_option = int(input("Choose: "))
        except ValueError:
            pass
        else:
            exec_menu = chargen_switcher.get(chosen_option, 0)
            if exec_menu != 0:
                if chosen_option == 1:
                    main_stats, stat_modifiers = exec_menu(main_stats)
                    level = 1
                    exp = 0
                    hp = 10 + stat_modifiers["VIG"]
                    mp = 20 + stat_modifiers["INT"]
                    print("hp: " + str(hp))
                    print("mp: " + str(mp))
                elif chosen_option == 2:
                    if main_stats == 0:
                        print("You still haven't set up your stats")
                        input(">...")
                    else:
                        if 'points' not in skill_list['skills'][0]:  # Check if Skill_list has updated fields
                            skill_count = 0
                            for i in skill_list['skills']:  # Add point and value field to every skill for assigned points
                                new_field = {'points': 0, 'value': stat_modifiers[i['stat']]}
                                skill_list['skills'][skill_count].update(new_field)
                                skill_count += 1
                        skill_list = exec_menu(skill_list, stat_modifiers)
                elif chosen_option == 3:
                    pass  # TODO
                elif chosen_option == 4:
                    pass  # TODO
                elif chosen_option == 5:
                    if main_stats == 0 or 'points' not in skill_list['skills'][0]:
                        print("You haven't set up your stats or skills")
                        input('>...')
                    else:
                        chargen_check = exec_menu()
                else:
                    pass

    # Menu for all chargen options
    # Generic menu confirmation function
    # Add inventory
    # Add Spells
    # Add Perks/Quirks?
    # Add Abilities?
    player = pl.Player(name, hp, mp, level, exp, main_stats, stat_modifiers, skill_list)
    print("\nPlayer data\n")
    print(player)
    print(dir(player))
    print(player.stats)
    print(player.stats_modifiers)
    for i in player.skills:
        print(player.skills[i])
    return player
