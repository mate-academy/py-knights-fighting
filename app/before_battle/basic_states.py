class New_Knight:
    def __init__(self, name, power, hp, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def improve_states(self,levelup):
        if len(levelup.armour) != 0:
            for i in range(len(levelup.armour)):
                self.protection += levelup.armour[i]['protection']

        for weapon in levelup.weapon:
            self.power += levelup.weapon['power']

        if levelup.potion is not None:
            if levelup.potion['effect'].get('power'):
                self.power += levelup.potion['effect']['power']
            if levelup.potion['effect'].get('hp'):
                self.hp += levelup.potion['effect']['hp']
            if levelup.potion['effect'].get('protection'):
                self.protection += levelup.potion['effect']['protection']

