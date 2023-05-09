from __future__ import annotations

from app.equipment.armour import ArmourPart
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    protection = 0

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def attack(self, enemy: Knight) -> None:
        enemy.hp -= self.power - enemy.protection
        enemy.hp = max(0, enemy.hp)

    def apply_armour(self, armour: list[ArmourPart]) -> None:
        for a_piece in armour:
            self.protection += a_piece.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        if potion.effects.get("hp"):
            self.hp += potion.effects["hp"]
        if potion.effects.get("power"):
            self.power += potion.effects["power"]
        if potion.effects.get("protection"):
            self.protection += potion.effects["protection"]

    def apply_equipment(self, armour_stats: list[dict], weapon_stats: dict,
                        potion_stats: dict | None) -> None:
        weapon = Weapon(weapon_stats["name"], weapon_stats["power"])
        self.apply_weapon(weapon)

        armour = [ArmourPart(a_piece["part"], a_piece["protection"])
                  for a_piece in armour_stats]
        self.apply_armour(armour)

        if potion_stats:
            potion = Potion(potion_stats["name"], potion_stats["effect"])
            self.apply_potion(potion)
