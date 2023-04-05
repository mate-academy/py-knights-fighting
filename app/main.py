from app.battle_knights.fighting import Battle
from app.creation_knights.knights_stats import Knight


Knights = {
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
    # creation of a dictionary generator of class knights
    knights_list = {
        name: Knight(
            characteristics["name"],
            characteristics["power"],
            characteristics["hp"],
            characteristics["armour"],
            characteristics["weapon"],
            characteristics["potion"])
        for name, characteristics in knights_config.items()
    }

    # application of characteristics
    for characteristics in knights_list.values():
        Knight.apply_weapon(characteristics)
        Knight.apply_armour(characteristics)
        Knight.apply_potion(characteristics)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle.combat(knights_list["lancelot"], knights_list["mordred"])

    # 2 Arthur vs Red Knight:
    Battle.combat(knights_list["arthur"], knights_list["red_knight"])

    # check if someone fell in battle
    Battle.check_death(knights_list)

    # Return battle results:
    return {
        knights_list["lancelot"].name: knights_list["lancelot"].hp,
        knights_list["arthur"].name: knights_list["arthur"].hp,
        knights_list["mordred"].name: knights_list["mordred"].hp,
        knights_list["red_knight"].name: knights_list["red_knight"].hp,
    }


print(battle(Knights))
