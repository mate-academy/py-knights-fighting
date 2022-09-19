class Armour:
    def __init__(self, armour: list):
        self.armour = armour
        self.protection = 0

    def apply_armor(self):
        for part in self.armour:
            self.protection += part["protection"]
        return self.protection


class Weapon:
    def __init__(self, weapon: dict):
        self.power = weapon["power"]

    def get_power(self):
        return self.power


class Potion:
    def __init__(self, potion: dict):
        self.potion = potion

    def apply_potion(self, other):
        if self.potion is not None:
            if self.potion["effect"].get("power"):
                other.power += self.potion["effect"]["power"]
            if self.potion["effect"].get("protection"):
                other.protection += self.potion["effect"]["protection"]
            if self.potion["effect"].get("hp"):
                other.hp += self.potion["effect"]["hp"]
