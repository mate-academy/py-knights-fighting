from app.knight.knight_class import Knight


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
    # KNIGHT PRESENTATION:
    kinghts = {name: Knight(knights[name]) for name in knights}

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    kinghts["lancelot"].battle(kinghts["mordred"])

    # 2 Arthur vs Red Knight:
    kinghts["arthur"].battle(kinghts["red_knight"])

    # Return battle results:
    return {
        kinghts["lancelot"].name: kinghts["lancelot"].hp,
        kinghts["arthur"].name: kinghts["arthur"].hp,
        kinghts["mordred"].name: kinghts["mordred"].hp,
        kinghts["red_knight"].name: kinghts["red_knight"].hp,
    }


result = battle(KNIGHTS)
print("Battle Results:\n")
for knight in result:
    hp = f"{result[knight]} HP" if result[knight] else "Was defeated"
    print(f"{knight} = {hp}")
