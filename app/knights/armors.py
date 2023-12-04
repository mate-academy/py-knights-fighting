class Armour:
    def __init__(self, part: str, protection: str) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: int) -> None:
        self.name = name
        self.effect = effect


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
