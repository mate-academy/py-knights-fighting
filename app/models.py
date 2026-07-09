
class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Knights:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: Weapon, potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
