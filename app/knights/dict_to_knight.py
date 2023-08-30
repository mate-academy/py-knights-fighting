from app.knights.Knight import Knight


def hero_initialise(information: dict) -> list[Knight]:
    heroes_name = ["lancelot", "arthur", "mordred", "red_knight"]
    stat_of_character = []
    for i in heroes_name:
        stat_of_character.append(
            Knight(
                information[f"{i}"]["name"],
                information[f"{i}"]["power"],
                0,
                information[f"{i}"]["hp"],
                information[f"{i}"]["armour"],
                information[f"{i}"]["weapon"],
                information[f"{i}"]["potion"]
            )
        )

    lancelot, arthur, mordred, red_knight = stat_of_character

    heroes_list = [lancelot, arthur, mordred, red_knight]
    return heroes_list


knights_info = {
    "lancelot": {
        "name": "Lancelot", "power": 35, "hp": 100,
        "armour": {
            "part": "helmet",
            "protection": 25,
        },
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur", "power": 45, "hp": 75,
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
        "name": "Mordred", "power": 30, "hp": 90,
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
        "name": "Red Knight", "power": 40, "hp": 70,
        "armour": {
            "part": "breastplate",
            "protection": 25,
        },
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
