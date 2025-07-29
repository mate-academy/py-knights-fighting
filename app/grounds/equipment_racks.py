class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(
        self,
        name: str,
        hp_effect: int,
        power_effect: int,
        protection_effect: int
    ) -> None:
        self.name = name
        self.hp_effect = hp_effect
        self.power_effect = power_effect
        self.protection_effect = protection_effect
