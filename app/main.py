from app.championship.knights import Knights


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


def battle(knights_config: dict) -> dict:

    list_knights = []
    for knight in knights_config:
        list_knights.append(Knights(
            name=knights_config[knight]["name"],
            power=knights_config[knight]["power"],
            hp=knights_config[knight]["hp"],
            armours=knights_config[knight]["armour"],
            weapon=knights_config[knight]["weapon"],
            potion=knights_config[knight]["potion"]
        ))

    list_knights[0].preparing_knight_battle()
    list_knights[1].preparing_knight_battle()
    list_knights[2].preparing_knight_battle()
    list_knights[3].preparing_knight_battle()

    list_knights[0].hp -= list_knights[2].power - list_knights[0].protection
    list_knights[2].hp -= list_knights[0].power - list_knights[2].protection

    list_knights[0].check_if_someone_fell_in_battle()
    list_knights[2].check_if_someone_fell_in_battle()

    list_knights[1].hp -= list_knights[3].power - list_knights[1].protection
    list_knights[3].hp -= list_knights[1].power - list_knights[3].protection

    list_knights[1].check_if_someone_fell_in_battle()
    list_knights[3].check_if_someone_fell_in_battle()

    return {
        list_knights[0].name: list_knights[0].hp,
        list_knights[1].name: list_knights[1].hp,
        list_knights[2].name: list_knights[2].hp,
        list_knights[3].name: list_knights[3].hp,
    }


print(battle(knights))
