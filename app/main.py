from app.cavaleiro import Cavaleiro


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


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights_collection = {}
    for knight_key in knights_config:
        knights_data = knights_config[knight_key]
        knight = Cavaleiro(
            knights_data["name"],
            knights_data["power"],
            knights_data["hp"],
            knights_data["armour"],
            knights_data["weapon"],
            knights_data["potion"]
        )

        # apply armour
        knight.calculate_protection()

        # apply weapon
        knight.calculate_weapon_power()

        # apply potion
        knight.apply_potion()

        knights_collection[knight_key] = knight

    battle_calculation(
        knights_collection["lancelot"],
        knights_collection["mordred"]
    )

    battle_calculation(
        knights_collection["arthur"],
        knights_collection["red_knight"]
    )

    lancelot = knights_collection["lancelot"]
    mordred = knights_collection["mordred"]
    arthur = knights_collection["arthur"]
    red_knight = knights_collection["red_knight"]

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


def battle_calculation(knight1: Cavaleiro, knight2: Cavaleiro) -> None:

    damage1 = knight1.power - knight2.protection
    knight2.hp -= damage1

    damage2 = knight2.power - knight1.protection
    knight1.hp -= damage2

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0
