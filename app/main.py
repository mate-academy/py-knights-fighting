from app.knights.prepare import Knight


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


def knights_fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    # check if someone fell in battle
    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_config["lancelot"]
    cl_lancelot = Knight(lancelot["name"], lancelot["power"],
                         lancelot["hp"], lancelot["armour"],
                         lancelot["weapon"], lancelot["potion"])
    cl_lancelot.prepare_for_battle()

    # arthur
    arthur = knights_config["arthur"]
    cl_arthur = Knight(arthur["name"], arthur["power"],
                       arthur["hp"], arthur["armour"],
                       arthur["weapon"], arthur["potion"])
    cl_arthur.prepare_for_battle()

    # mordred
    mordred = knights_config["mordred"]
    cl_mordred = Knight(mordred["name"], mordred["power"],
                        mordred["hp"], mordred["armour"],
                        mordred["weapon"], mordred["potion"])
    cl_mordred.prepare_for_battle()

    # red_knight
    red_knight = knights_config["red_knight"]
    cl_red_knight = Knight(red_knight["name"], red_knight["power"],
                           red_knight["hp"], red_knight["armour"],
                           red_knight["weapon"], red_knight["potion"])
    cl_red_knight.prepare_for_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights_fight(cl_lancelot, cl_mordred)

    # 2 Arthur vs Red Knight:
    knights_fight(cl_arthur, cl_red_knight)

    # Return battle results:
    return {
        cl_lancelot.name: cl_lancelot.hp,
        cl_arthur.name: cl_arthur.hp,
        cl_mordred.name: cl_mordred.hp,
        cl_red_knight.name: cl_red_knight.hp,
    }


print(battle(KNIGHTS))
