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
            effects: dict
    ) -> None:
        self.name = name
        self.power = effects.get("power", 0)
        self.hp = effects.get("hp", 0)
        self.protection = effects.get("protection", 0)
