class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effects: dict) -> None:
        self.name = name
        self.effects = effects


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
