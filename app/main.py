from app.knights import Knight
from app.knights_battle import KnightsBattle

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
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot_class = Knight(knights_config["lancelot"])
    lancelot_class.prepare_for_battle()

    # arthur
    arthur_class = Knight(knights_config["arthur"])
    arthur_class.prepare_for_battle()

    # mordred
    mordred_class = Knight(knights_config["mordred"])
    mordred_class.prepare_for_battle()

    # red_knight
    red_knight_class = Knight(knights_config["red_knight"])
    red_knight_class.prepare_for_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    first_fight = KnightsBattle(lancelot_class, mordred_class)
    first_fight.make_a_battle()
    first_fight.check_results()

    # 2 Arthur vs Red Knight:
    second_fight = KnightsBattle(arthur_class, red_knight_class)
    second_fight.make_a_battle()
    second_fight.check_results()

    # Return battle results:
    return {
        lancelot_class.name: lancelot_class.hp,
        arthur_class.name: arthur_class.hp,
        mordred_class.name: mordred_class.hp,
        red_knight_class.name: red_knight_class.hp,
    }


print(battle(KNIGHTS))
