from __future__ import annotations
from app.knights import Knight
from app.equipment.weapons import Weapon
from app.equipment.armour import Armour
from app.equipment.consumable import Potion


def knight_initialization(knights: dict) -> dict:
    participants = {}

    for stats in knights.values():
        knight = Knight(
            stats.pop("name"),
            stats.pop("hp"),
            stats.pop("power"),
            0
        )

        participants[knight] = stats

    return participants


def preparations(knights: dict) -> list[Knight]:
    prepared_knights = []

    for knight, equipment in knights.items():
        weapon = Weapon(equipment["weapon"])
        weapon.equip_weapon(knight)

        for item in equipment["armour"]:
            piece = Armour(item)
            piece.equip_armour(knight)

        if equipment["potion"]:
            knight.drank_pot(Potion(equipment["potion"]))

        prepared_knights.append(knight)

    return prepared_knights


def battle(knights: dict) -> dict:
    base_knights = knight_initialization(knights)
    result = {}
    opponent = {
        "Lancelot": "Mordred",
        "Mordred": "Lancelot",
        "Arthur": "Red Knight",
        "Red Knight": "Arthur"
    }

    for knight in preparations(base_knights):
        knight.versus(Knight.knights[opponent[knight.name]])
        if knight.hp < 0:
            knight.hp = 0
        result[knight.name] = knight.hp

    return result
