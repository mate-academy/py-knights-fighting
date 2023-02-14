class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: dict) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def check_for_effect(self, stat: str) -> bool:
        return stat in self.effect
