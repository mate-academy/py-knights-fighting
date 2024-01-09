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


def apply_armor(character: dict) -> None:
    character["protection"] = sum(armor["protection"] for armor in character["armour"])  # noqa: E501


def apply_weapon(character: dict) -> None:
    character["power"] += character["weapon"]["power"]


def apply_potion(character: dict) -> None:
    potion = character.get("potion")
    if potion:
        effect = potion.get("effect", {})
        character["power"] += effect.get("power", 0)
        character["protection"] += effect.get("protection", 0)
        character["hp"] += effect.get("hp", 0)


def prepare_character(character: dict) -> None:
    apply_armor(character)
    apply_weapon(character)
    apply_potion(character)


def battle_round(attacker: dict, defender: dict) -> None:
    defender["hp"] -= max(attacker["power"] - defender["protection"], 0)


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    for knight in knights_config.values():
        prepare_character(knight)

    # BATTLE:
    battle_round(knights_config["lancelot"], knights_config["mordred"])
    battle_round(knights_config["arthur"], knights_config["red_knight"])

    # Check if someone fell in battle
    for knight in knights_config.values():
        knight["hp"] = max(0, knight["hp"])

    # Return battle results:
    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


print(battle(KNIGHTS))
