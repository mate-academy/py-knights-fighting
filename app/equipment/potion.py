class Potion:
    def __init__(self, name: str, power: int = 0,
                 protection: int = 0, hp: int = 0) -> None:
        self.name = name
        self.power_effect = power
        self.protection_effect = protection
        self.hp_effect = hp
