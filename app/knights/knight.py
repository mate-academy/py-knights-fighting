class Knight:

    all_knights = {}

    def __init__(self, name, power, hp, weapon,
                 armour=None, potion=None, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.__class__.all_knights[name] = self
