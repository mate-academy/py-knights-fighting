class New_Knight:
    def __init__(self, name, power, hp, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def improve_stats(self, levelup):
        if len(levelup.armour) != 0:
            for i in range(len(levelup.armour)):
                self.protection += levelup.armour[i]['protection']

        self.power += levelup.weapon['power']

        stats = ("power", "hp", "protection")
        if levelup.potion is not None:
            self.power += levelup.potion['effect'].get(stats[0], 0)
            self.hp += levelup.potion['effect'].get(stats[1], 0)
            self.protection += levelup.potion['effect'].get(stats[2], 0)
