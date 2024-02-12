from app.kingdom.battle_zone import Battle
from app.kingdom.knight_prepare import Knights

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


def battle(knights_configuration: dict) -> dict:
    inst_knights = []

    # create knights instance
    for knight, options in knights_configuration.items():
        inst_knights.append(Knights(name=options["name"],
                                    power=options["power"],
                                    hp=options["hp"],
                                    armour=options["armour"],
                                    weapon=options["weapon"],
                                    potion=options["potion"]))
    # All Prepare
    for knight in inst_knights:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    # All Battle
    Battle.battle_round(inst_knights[0], inst_knights[2])
    Battle.battle_round(inst_knights[1], inst_knights[3])
    print(Battle.battle_result)
    # need return
    return Battle.battle_result


battle(KNIGHTS)
