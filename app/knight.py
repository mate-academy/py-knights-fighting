"""
Docstring for Kodree.github_tasks.py-knights-fighting.pkg.knight

Define custom classes for knights fighting application.
"""


class ArmourPiece:
    def __init__(
            self,
            part: str,
            protection: int
    ) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(
            self,
            name: str,
            power: int
    ) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
            self,
            name: str,
            effect: dict
    ) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[ArmourPiece] | None,
            weapon: Weapon,
            potion: Potion | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = 0
        if self.armour is not None:
            for armour_piece in self.armour:
                self.protection += armour_piece.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
