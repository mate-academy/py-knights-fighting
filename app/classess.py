class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection


class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
