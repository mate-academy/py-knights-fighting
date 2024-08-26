from app.knight import Knight


def battle(knights_config: dict) -> dict:
    result = {}

    for element in knights_config:
        knight = Knight(name="", power=0, hp=0, protection=0)
        knight.adding_value_to_instance(knights_config[element])
        result[knight.name] = knight

    battle_list = ["Lancelot", "Mordred", "Arthur", "Red Knight"]

    for i in range(0, len(battle_list) // 2 + 1, 2):
        result[battle_list[i]].fight(result[battle_list[i + 1]])

    for i in range(len(battle_list)):
        result[battle_list[i]].check_if_someone_fell_in_battle()

    return {
        result["Lancelot"].name: result["Lancelot"].hp,
        result["Arthur"].name: result["Arthur"].hp,
        result["Mordred"].name: result["Mordred"].hp,
        result["Red Knight"].name: result["Red Knight"].hp,
    }


KNIGHT = {
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

print(battle(knights_config=KNIGHT))
