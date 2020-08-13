class Player():
    def __init__(self, name, hp, mp, lvl, xp, stats, modifiers, skill_list):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.lvl = lvl
        self.xp = xp
        self.stats = stats
        self.stats_modifiers = modifiers
        self.skills = {}
        for i in skill_list['skills']:
            skill_item = {i['id']: Skill(i['id'], i['stat'], i['points'], i['value'], self.stats_modifiers[i['stat']])}
            self.skills.update(skill_item)

    def __str__(self):
        return "Player Object with name: " + self.name


class Skill():
    def __init__(self, name, stat, points, value, stat_modifier):
        self.name = name
        self.stat = stat
        self.points = points
        self.modifier = stat_modifier
        self.value = value

    def __str__(self):
        return "Skill Object: " + self.name + " - " + str(self.value) + " - " + str(self.points) + " - " + self.stat + " - " + str(self.modifier)

    def update_value(self, stat_modifier):
        self.value = stat_modifier + self.points

    def print_self(self):
        print(self.stat + " - " + str(self.points) + " - " + str(self.value))
