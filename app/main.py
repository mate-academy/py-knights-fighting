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


def battle(knights: dict) -> dict:
    dict_knights = {}

    def perform_combat_between_knights(
            attacker_name: str,
            defender_name: str
    ) -> None:
        attacker = dict_knights[attacker_name]
        defender = dict_knights[defender_name]

        attacker.hp -= max(defender.power - attacker.protection, 0)
        defender.hp -= max(attacker.power - defender.protection, 0)

    for knight, value in knights.items():
        knight_obj = Knight(
            value["name"],
            value["power"],
            value["hp"]
        )

        Knight.prepare(
            knight_obj,
            value["armour"],
            value["weapon"],
            value["potion"]
        )
        dict_knights[knight] = knight_obj

    perform_combat_between_knights("lancelot", "mordred")
    perform_combat_between_knights("arthur", "red_knight")

    for knight in dict_knights.values():
        knight.hp = max(0, knight.hp)

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in dict_knights.values()
    }


print(battle(KNIGHTS))
