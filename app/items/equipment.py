class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.power = power
        self.name = name


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.protection = protection
        self.name = name


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect
