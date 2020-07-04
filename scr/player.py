class Player():
    def __init__(self, name, hp, mp, lvl, xp, stats):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.lvl = lvl
        self.xp = xp
        self.stats = stats

    def __str__(self):
        return "Player Object with name: " + self.name
