from app.battle_preparation import KnightPreparation
from app.battle import Battle

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


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = KnightPreparation(knightsconfig["lancelot"])
    lancelot.prepare_knight()

    arthur = KnightPreparation(knightsconfig["arthur"])
    arthur.prepare_knight()

    mordred = KnightPreparation(knightsconfig["mordred"])
    mordred.prepare_knight()

    red_knight = KnightPreparation(knightsconfig["red_knight"])
    red_knight.prepare_knight()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle1 = Battle(lancelot, mordred)
    battle1.battle()

    # 2 Arthur vs Red Knight:
    battle2 = Battle(arthur, red_knight)
    battle2.battle()

    # Return battle results:
    return {
        lancelot.knight_info["name"]: lancelot.knight_info["hp"],
        arthur.knight_info["name"]: arthur.knight_info["hp"],
        mordred.knight_info["name"]: mordred.knight_info["hp"],
        red_knight.knight_info["name"]: red_knight.knight_info["hp"],
    }


print(battle(KNIGHTS))
