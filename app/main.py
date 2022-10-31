from app.apply.armour import apply_armour
from app.apply.potion import apply_potion
from app.apply.weapon import apply_weapon
from app.battle.fell_in_battle import fell_in_battle
from app.battle.fight import fight
from app.battle.result import battle_result


knights_config = {
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
    # BATTLE PREPARATIONS:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    knights = (lancelot, arthur, mordred, red_knight)
    for knight in knights:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)
    fight(mordred, lancelot)

    # check if someone fell in battle
    fell_in_battle(lancelot)
    fell_in_battle(mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)
    fight(red_knight, arthur)

    # check if someone fell in battle
    fell_in_battle(arthur)
    fell_in_battle(red_knight)

    # Return battle results:
    return battle_result(knights_config)


print(battle(knights_config))
