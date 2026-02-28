class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
            self,
            name: str,
            health: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.protection = protection
