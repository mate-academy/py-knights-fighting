class Potion:
    power: int = 0
    hp: int = 0
    protection: int = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def prepare(self, power: int, hp: int, protection: int) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection
