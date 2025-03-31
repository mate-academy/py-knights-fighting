class Knight:
    def __init__(self, name, power, hp, armour=None, weapon=None, potion=None):
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.calculate_final_stats()

    def calculate_final_stats(self):
        self.protection = sum(part.protection for part in self.armour)
        self.power = self.base_power + (self.weapon.power if self.weapon else 0)
        self.hp = self.base_hp
        if self.potion:
            potion_effects = self.potion.effect
            self.hp += potion_effects.get("hp", 0)
            self.power += potion_effects.get("power", 0)
            self.protection += potion_effects.get("protection", 0)


class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
