from app.Preparation.Knights import Knight
from app.Battle.fights import fight


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

    lancelot_value = knights_config["lancelot"]
    lancelot = Knight(lancelot_value["name"], lancelot_value["power"],
                      lancelot_value["hp"], lancelot_value["weapon"]["power"])
    lancelot.apply_armour(lancelot_value["armour"])
    if lancelot_value["potion"]:
        lancelot.apply_potion(lancelot_value["potion"]["effect"])

    arthur_value = knights_config["arthur"]
    arthur = Knight(arthur_value["name"], arthur_value["power"],
                    arthur_value["hp"], arthur_value["weapon"]["power"])
    arthur.apply_armour(arthur_value["armour"])
    if arthur_value["potion"]:
        arthur.apply_potion(arthur_value["potion"]["effect"])

    mordred_value = knights_config["mordred"]
    mordred = Knight(mordred_value["name"], mordred_value["power"],
                     mordred_value["hp"], mordred_value["weapon"]["power"])
    mordred.apply_armour(mordred_value["armour"])
    if mordred_value["potion"]:
        mordred.apply_potion(mordred_value["potion"]["effect"])

    red_knight_value = knights_config["red_knight"]
    red_knight = Knight(red_knight_value["name"], red_knight_value["power"],
                        red_knight_value["hp"],
                        red_knight_value["weapon"]["power"])
    red_knight.apply_armour(red_knight_value["armour"])
    if red_knight_value["potion"]:
        red_knight.apply_potion(red_knight_value["potion"]["effect"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
