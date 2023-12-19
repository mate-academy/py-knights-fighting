class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_potion_effects(self):
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)

    def total_protection(self):
        return sum(armour.protection for armour in self.armour)


class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
