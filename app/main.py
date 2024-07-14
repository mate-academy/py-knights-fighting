from app.items import Armor, Weapon, Potion
from app.knight import Knight


def battle(knights_stats: dict) -> None:
    knight_instances = []
    for knight_stats in knights_stats.values():
        knight_instances.append(
            Knight(knight_stats["name"],
                   knight_stats["power"],
                   knight_stats["hp"],
                   [Armor(**arm) for arm in knight_stats["armour"]],
                   Weapon(knight_stats["weapon"]["name"],
                   knight_stats["weapon"]["power"]),
                   Potion(knight_stats["potion"]["name"],
                   knight_stats["potion"]["effect"])
                   if knight_stats["potion"] else None))

    for knight in knight_instances:
        knight.prepare_for_battle()

    lancelot = knight_instances[0]
    mordred = knight_instances[2]
    lancelot.receive_damage(mordred.power - lancelot.protection)
    mordred.receive_damage(lancelot.power - mordred.protection)

    arthur = knight_instances[1]
    red_knight = knight_instances[3]
    arthur.receive_damage(red_knight.power - arthur.protection)
    red_knight.receive_damage(arthur.power - red_knight.protection)

    return {knight.name: knight.hp for knight in knight_instances}


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

print(battle(KNIGHTS))
