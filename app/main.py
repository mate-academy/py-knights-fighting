from app.classess.khight import Knight


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

    knights = []

    # BATTLE PREPARATIONS:
    for knight_name, knight_info in list(knights_config.items()):

        protection = 0
        for el in knights_config[knight_name]["armour"]:
            if "protection" in el:
                protection += el["protection"]

        knights_config[knight_name]["power"] += (
            knights_config)[knight_name]["weapon"]["power"]

        if knights_config[knight_name]["potion"] is not None:
            knights_config[knight_name]["hp"] += (
                knights_config)[knight_name]["potion"]["effect"]["hp"]

            knights_config[knight_name]["power"] += (
                knights_config)[knight_name]["potion"]["effect"]["power"]

            if "protection" in knights_config[knight_name]["potion"]["effect"]:
                protection += (
                    knights_config
                )[knight_name]["potion"]["effect"]["protection"]

        # initialization knight
        knights.append(Knight(name=knight_info["name"],
                              power=knight_info["power"],
                              hp=knight_info["hp"],
                              protection=protection))

    lancelot, arthur, mordred, red_knight = knights

    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot.battle(mordred)
    arthur.battle(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
