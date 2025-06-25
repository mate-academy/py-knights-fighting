from modules.knight import Knight
from modules.arsenal import Weapon, Armor, Potion


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
    list_of_knights = []

    for knight_data in knightsconfig.values():
        armor_list = [
            Armor(ar["part"], ar["protection"])
            for ar in knight_data["armour"]
        ]

        weapon = Weapon(
            knight_data["weapon"]["name"],
            knight_data["weapon"]["power"]
        )

        potion = (
            Potion(
                knight_data["potion"]["name"],
                knight_data["potion"]["effect"]
            )
            if knight_data["potion"] is not None else None
        )

        knight = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armor=armor_list,
            weapon=weapon,
            potion=potion
        )
        list_of_knights.append(knight)

    lancelot = list_of_knights[0]
    arthur = list_of_knights[1]
    mordred = list_of_knights[2]
    red_knight = list_of_knights[3]

    print("First Fight:")
    print()
    lancelot.fight_with(mordred)
    print()
    print("Other Fight:")
    print()
    arthur.fight_with(red_knight)
    print()

    res_dict = {"Lancelot": lancelot.hp, "Arthur": arthur.hp,
                "Mordred": mordred.hp, "Red Knight": red_knight.hp}

    return res_dict
