class Potion:
    def __init__(self, name: str, power: int, hp: int, protection: int) -> None:
        self.name = name
        self.power = power or 0
        self.hp = hp or 0
        self.protection = protection or 0