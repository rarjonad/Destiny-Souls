class Player():
    def __init__(self, name, hp, mp, lvl, xp, stats, modifiers):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.lvl = lvl
        self.xp = xp
        self.stats = stats
        self.stats_modifiers = modifiers

    def __str__(self):
        return "Player Object with name: " + self.name
