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
            self, name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


class Knights:
    all_knights = {}

    def __init__(
            self, name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: "Weapon",
            potion: None | Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        Knights.all_knights[name] = self
