from app.prepare.protection import Knight

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


def get_knight(name: str, config: dict):
    return Knight(config[name]["name"],
                  config[name]["power"],
                  config[name]["hp"])


def battle_two_knights(first: Knight, second: Knight):
    first.hp -= second.power - first.protection
    if first.hp <= 0:
        first.hp = 0
    second.hp -= first.power - second.protection
    if second.hp <= 0:
        second.hp = 0
    return {first.name: first.hp, second.name: second.hp}


def battle(knights_config):
    lancelot = get_knight("lancelot", knights_config)
    arthur = get_knight("arthur", knights_config)
    mordred = get_knight("mordred", knights_config)
    red_knight = get_knight("red_knight", knights_config)
    knights_list = [lancelot, arthur, mordred, red_knight]
    for knight in knights_list:
        for value in knights_config.values():
            if knight.name == value["name"]:
                knight.get_armour(value["armour"])
                knight.get_weapon(value["weapon"])
                knight.get_potion(value["potion"])
    first_result = battle_two_knights(lancelot, mordred)
    second_result = battle_two_knights(arthur, red_knight)
    return first_result | second_result


print(battle(KNIGHTS))
