from typing import Optional


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.hp: int = base_hp
        self.power: int = base_power
        self.protection: int = 0

        self.apply_armour(armour)
        self.apply_weapon(weapon)
        self.apply_potion(potion)

    def apply_armour(self, armour: list[Armour]) -> None:
        self.protection = sum(part.protection for part in armour)

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Optional[Potion]) -> None:
        if not potion:
            return
        self.hp += potion.effect.get("hp", 0)
        self.power += potion.effect.get("power", 0)
        self.protection += potion.effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
