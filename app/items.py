class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.name = part
        self.protection = protection


class PotionEffect:
    def __init__(
            self,
            hp: int = 0,
            power: int = 0,
            protection: int = 0
    ) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect: PotionEffect = PotionEffect(**effect)
