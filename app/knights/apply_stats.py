from __future__ import annotations
from app.knights.knight_stats import Knight


def apply_potion(knight: Knight) -> None:
    for stat, value in knight.potion.get("effect").items():
        knight.stat += value

def apply_armour(knight: Knight) -> None:
    for armour_part in knight.armour:
        knight.protection += armour_part.get("protection")

def apply_weapon(knight: Knight) -> None:
    for weapon in knight.weapon:
        knight.power += weapon.get("power")
