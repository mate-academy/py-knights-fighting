from __future__ import annotations
from app.models.equipment import Weapon, Potion, ArmourPiece


class Knight:
    def __init__(self, name: str, base_power: int,
                 base_hp: int, armour: list[ArmourPiece],
                 weapon: Weapon, potion: Potion | None = None) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def calculate_protection(self) -> int:
        protection = 0
        for armour_piece in self.armour:
            protection += armour_piece.protection
        return protection

    def calculate_power(self) -> int:
        return self.base_power + self.weapon.power

    def calculate_hp(self) -> int:
        hp = self.base_hp
        if self.potion:
            hp += self.potion.effect.hp
        return max(0, hp)

    def get_battle_stats(self) -> dict:
        stats = {
            "name": self.name,
            "hp": self.calculate_hp(),
            "power": self.calculate_power(),
            "protection": self.calculate_protection()
        }
        if self.potion:
            stats["power"] += self.potion.effect.power
            stats["protection"] += self.potion.effect.protection

        stats["power"] = max(0, stats["power"])
        stats["protection"] = max(0, stats["protection"])

        return stats

    def __str__(self) -> str:
        return f"Лицар {self.name}"
