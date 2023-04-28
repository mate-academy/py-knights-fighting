class Weapon:
    def __init__(self, name: str, power: int) -> object:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int):
        self.name = part
        self.protection = protection


class PotionEffect:
    def __init__(self, hp=0, power=0, protection=0):
        self.hp = hp
        self.power = power
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect: PotionEffect = PotionEffect(**effect)
