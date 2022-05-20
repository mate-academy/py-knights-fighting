from app.knight_general_characteristic import Knight


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


# Function which create Knight instances
def add_a_knight(name: str, config: dict):
    return Knight(config[name]["name"],
                  config[name]["power"],
                  config[name]["hp"])


def result_of_fight_two_opponents(first_opponent: Knight,
                                  second_opponent: Knight):
    first_opponent.hp -= second_opponent.power - first_opponent.protection
    if first_opponent.hp <= 0:
        first_opponent.hp = 0
    second_opponent.hp -= first_opponent.power - second_opponent.protection
    if second_opponent.hp <= 0:
        second_opponent.hp = 0

    return {
        first_opponent.name: first_opponent.hp,
        second_opponent.name: second_opponent.hp
    }


def battle(knights_config):

    # Prepare to battle:

    # 1) Create knights
    lancelot = add_a_knight("lancelot", knights_config)
    arthur = add_a_knight("arthur", knights_config)
    mordred = add_a_knight("mordred", knights_config)
    red_knight = add_a_knight("red_knight", knights_config)

    # 2) Create list if knights
    knights_list = [lancelot, arthur, mordred, red_knight]

    # 3) Add  armour, weapon, potion to knights
    for knight in knights_list:
        for characteristic in knights_config.values():
            if knight.name == characteristic["name"]:
                knight.add_armour(characteristic["armour"])
                knight.add_weapon(characteristic["weapon"])
                knight.add_potion(characteristic["potion"])

    # Let start the battle and get results of fights:

    # 1) First fight result:
    first_fight_result = result_of_fight_two_opponents(lancelot, mordred)

    # 2) Second fight result
    second_fight_result = result_of_fight_two_opponents(arthur, red_knight)

    # Return a result of the battle:
    return first_fight_result | second_fight_result
