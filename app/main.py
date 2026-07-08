from app.preparation.health import calculate_hp
from app.preparation.armour import apply_armour
from app.preparation.power import get_power
from app.fight.knights_fight import two_knights_fight

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
            },
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
            },
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
            },
        },
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def battle(knights_config: dict) -> dict:
    prepared_data = {}

    calculators = {
        "hp": calculate_hp,
        "power": get_power,
        "protection": apply_armour,
    }

    for knight in knights_config:
        prepared_data[knight] = {
            "name": knights_config[knight]["name"],
            **{
                stat: func(knights_config, knight)
                for stat, func in calculators.items()
            },
        }

    two_knights_fight(prepared_data["lancelot"], prepared_data["mordred"])
    two_knights_fight(prepared_data["arthur"], prepared_data["red_knight"])

    return {
        prepared_data[knight]["name"]: prepared_data[knight]["hp"]
        for knight in prepared_data
    }


print(battle(KNIGHTS))
