# models.py
class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self, name: str, base_power: int, base_hp: int,
        armour: list, weapon: Weapon, potion: Potion = None
    ) -> None:
        self.name = name
        self.power = base_power + weapon.power
        self.hp = base_hp
        self.protection = sum(a.protection for a in armour)
        if potion:
            self.hp += potion.effect.get("hp", 0)
            self.power += potion.effect.get("power", 0)
            self.protection += potion.effect.get("protection", 0)
