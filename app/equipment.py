class Armour:
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    def apply_armor(self, other):
        other.protection += self.protection


class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def apply_weapon(self, other):
        other.power += self.power


class Potion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect = effect

    def apply_potion(self, other):
        if self.effect.get('hp'):
            other.hp += self.effect['hp']
        if self.effect.get('power'):
            other.power += self.effect['power']
        if self.effect.get('protection'):
            other.protection += self.effect['protection']
