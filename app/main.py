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
        # print(f"Duel between {knights[first].name}
        # and {knights[second].name}")
        for _ in range(2):
            # print(f"{duelist[0].name} hp before fight: {duelist[0].hp}")
            duelist[0].hp -= (duelist[1].power - duelist[0].protection)

            if duelist[0].hp <= 0:
                duelist[0].hp = 0
                print(f"{duelist[0].name} has lost this fight.")

            result.update({duelist[0].name: duelist[0].hp})
            # print(f"{duelist[0].name} hp after fight: {duelist[0].hp}")
            duelist.reverse()

    print(result)
    return result


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


battle(KNIGHTS)
