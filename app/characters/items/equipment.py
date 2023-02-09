class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

class Weapon:
    def __init__(self, name: str, power: dict) -> None:
        self.name = name
        self.power = power
