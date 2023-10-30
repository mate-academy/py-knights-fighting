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

        participants.update({knight: stats})

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
            potion = Potion(equipment["potion"])
            knight.drank_pot(potion)

        prepared_knights.append(knight)

    return prepared_knights


def battle(knights: dict) -> dict:
    result = {}
    base_knights = knight_initialization(knights)
    prepared_knights = preparations(base_knights)

    for first in range(2):
        second = first + 2
        duelist = [prepared_knights[first], prepared_knights[second]]

        for _ in range(2):
            duelist[0].hp -= (duelist[1].power - duelist[0].protection)

            if duelist[0].hp <= 0:
                duelist[0].hp = 0

            result.update({duelist[0].name: duelist[0].hp})
            duelist.reverse()

    return result
