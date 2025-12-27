class Armour:
    def __init__(self, armours: list) -> None:
        self.armours = armours

    def total_protection(self) -> int:
        return sum(armour["protection"] for armour in self.armours)


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            protection: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
