from app.knights.potion import Potion
from app.knights.weapon import Weapon


def battle_preparation(knights: dict):
    for knight_name in knights:
        for armour in knights[knight_name]["armour"]:
            knights[knight_name]["protection"] += armour["protection"]

            # set protection to 0 if no armour is applied
        if "protection" not in knights[knight_name]:
            knights["lancelot"].get("protection", 0)

    # apply weapon
    for knight_name in knights:
        knight = knights[knight_name]
        Weapon.power_calculation(knight)

    # apply potion if exist
    for knight_name in knights:
        knight = knights[knight_name]
        if knight.potion is not None:
            Potion.apply_potion(knight)

    # -------------------------------------------------------------------------------
    # BATTLE:
def battle(knights):

    # 1 Lancelot vs Mordred:
    knights["lancelot"]["hp"] -= knights["mordred"]["power"] - knights["lancelot"].get("protection", 0)
    knights["mordred"]["hp"] -= knights["lancelot"]["power"] - knights["mordred"]["protection"]


    # check if someone fell in battle
    if knights["lancelot"]["hp"] <= 0:
        knights["lancelot"]["hp"] = 0

    if knights["mordred"]["hp"] <= 0:
        knights["mordred"]["hp"] = 0

    # Return battle results:
    return {
        knights["lancelot"]["name"]: knights["lancelot"]["hp"],
        knights["mordred"]["name"]: knights["mordred"]["hp"],
    }


knights = {
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
        "name": "Artur",
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

print(battle(knights))
