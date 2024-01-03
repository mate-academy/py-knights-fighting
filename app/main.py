from typing import Dict, List, Union


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


Knight_Config = Dict[str, Union[str, int, List[Dict[str, Union[str, int]]], Dict[str, Union[str, int, Dict[str, int]]]]]
Effect = Dict[str, int]


def apply_effects(character: Knight_Config) -> None:

    character["protection"] = sum([a["protection"] for a in character["armour"]])

    # apply weapon
    character["power"] += character["weapon"]["power"]

    # apply potion if exists
    if character["potion"] is not None:
        for effect_type, value in character["potion"]["effect"].items():
            if effect_type in character:
                character[effect_type] += value


def battle(knights_config: Dict[str, Knight_Config]) -> Dict[str, int]:

    for knight in knights_config.values():
        apply_effects(knight)

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for attacker_name, defender_name in battles:
        attacker = knights_config[attacker_name]
        defender = knights_config[defender_name]

        damage_to_defender = max(attacker["power"] - defender["protection"], 0)
        damage_to_attacker = max(defender["power"] - attacker["protection"], 0)

        defender["hp"] -= damage_to_defender
        attacker["hp"] -= damage_to_attacker

        defender["hp"] = max(defender["hp"], 0)
        attacker["hp"] = max(attacker["hp"], 0)

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


print(battle(KNIGHTS))
