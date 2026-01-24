from app.knights.knight import Knight

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
    # -------------------------------------------------------------------------------
    # BATTLE:
    knights_dict = {}
    for knight_name, knight in knights_config.items():
        knights_dict[knight_name] = Knight(
            knight["power"],
            knight["hp"],
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        )
    # 1 Lancelot vs Mordred:
    knights_dict["lancelot"].battle_vs(knights_dict["mordred"])
    knights_dict["mordred"].battle_vs(knights_dict["lancelot"])

    knights_dict["arthur"].battle_vs(knights_dict["red_knight"])
    knights_dict["red_knight"].battle_vs(knights_dict["arthur"])

    result_dict = {}
    for knight_name, knight in knights_dict.items():
        if "_" in knight_name:
            new_knight_name = knight_name.replace("_", " ")
            result_dict[new_knight_name.title()] = knight.hp
        else:
            result_dict[knight_name.capitalize()] = knight.hp

    # Return battle results:
    return result_dict


print(battle(KNIGHTS))
