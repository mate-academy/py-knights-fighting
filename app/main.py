from app.people.knights import Knight

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


def battle(knights: dict) -> dict:
    all_knight = {}
    for name, value in knights.items():
        knight = Knight(
            value["name"],
            value["power"],
            value["hp"],
            value["armour"],
            value["weapon"],
            value["potion"])
        all_knight[name] = knight
    for person in all_knight.values():
        person.weapon_up()
        person.armour_up()
        person.drink_potion()
    all_knight["lancelot"].battle(all_knight["mordred"])
    all_knight["arthur"].battle(all_knight["red_knight"])
    return {
        all_knight["lancelot"].name: all_knight["lancelot"].hp,
        all_knight["arthur"].name: all_knight["arthur"].hp,
        all_knight["mordred"].name: all_knight["mordred"].hp,
        all_knight["red_knight"].name: all_knight["red_knight"].hp,
    }


print(battle(KNIGHTS))
