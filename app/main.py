from app.fighters.knights_stat import Knight
from app.fighters.equipment import Weapon


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
list_of_knights: list["Knight"] = []
for key in KNIGHTS:
    list_of_knights.append(
        Knight
        (
            KNIGHTS[key]["name"],
            KNIGHTS[key]["power"],
            KNIGHTS[key]["hp"],
            Knight.create_list_armour(KNIGHTS[key]["armour"]),
            Weapon(KNIGHTS[key]["weapon"]["name"],
                   KNIGHTS[key]["weapon"]["power"]),
            Knight.create_potion(KNIGHTS[key]["potion"])
        )
    )


# -------------------------------------------------------------------------------
    # BATTLE:
def battle(list_fighters: list[Knight]) -> dict:

    for knight in list_fighters:
        knight.prepare_for_battle()

    # 1 Lancelot vs Mordred:
    lancelot = Knight.check_name(list_fighters, "Lancelot")
    mordred = Knight.check_name(list_fighters, "Mordred")
    lancelot.fight_between_two(mordred)

    # check if someone fell in battle
    lancelot.check_hp()
    mordred.check_hp()

    # 2 Arthur vs Red Knight:
    arthur = Knight.check_name(list_fighters, "Arthur")
    red_knight = Knight.check_name(list_fighters, "Red Knight")
    arthur.fight_between_two(red_knight)

    # check if someone fell in battle
    arthur.check_hp()
    red_knight.check_hp()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(list_of_knights))
