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


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights_collection = {}
    for knight_key in knightsconfig:
        knights_data = knightsconfig[knight_key]
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

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot = knights_collection["lancelot"]
    mordred = knights_collection["mordred"]

    damage = lancelot.power - mordred.protection
    mordred.hp -= damage

    damage = mordred.power - lancelot.protection
    lancelot.hp -= damage

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur = knights_collection["arthur"]
    red_knight = knights_collection["red_knight"]

    damage = arthur.power - red_knight.protection
    red_knight.hp -= damage

    damage = red_knight.power - arthur.protection
    arthur.hp -= damage

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
