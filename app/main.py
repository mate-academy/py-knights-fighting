from app.knight import Knight, fight
from app.accessories import Armour, Weapon, Potion


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
    list_of_knights = []
    for knight in knights_config.values():

        # creating instance of class Knight for each of the knights
        list_of_knights.append(Knight(
            knight["name"],
            knight["power"],
            knight["hp"]
        ))

        # applying armour, weapon and potion for each knight
        if knight["armour"] is not None:
            list_of_knights[-1].apply_armour(Armour(knight["armour"]))
        list_of_knights[-1].apply_weapon(Weapon(
            knight["weapon"]["name"],
            knight["weapon"]["power"]
        ))
        if knight["potion"] is not None:
            list_of_knights[-1].apply_potion(Potion(
                name=knight["potion"]["name"],
                hp=knight["potion"]["effect"].get("hp", 0),
                power=knight["potion"]["effect"].get("power", 0),
                protection=knight["potion"]["effect"].get("protection", 0)
            ))

    # battles
    fight(list_of_knights[0], list_of_knights[2])
    fight(list_of_knights[1], list_of_knights[3])

    # Return battle results:
    return {knight.name: knight.hp for knight in list_of_knights}


print(battle(KNIGHTS))
