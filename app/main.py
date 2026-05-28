from typing import Any

KnightConfig = dict[str, Any]
PreparedKnight = dict[str, Any]


KNIGHTS: dict[str, KnightConfig] = {
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
                "power": 15,
                "hp": -5,
                "protection": 10,
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
            },
        ],
        "weapon": {
            "name": "Sword",
            "power": 45,
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": 10,
                "power": 5,
            },
        },
    },
}


def prepare_knight(knight: KnightConfig) -> PreparedKnight:
    prepared_knight = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"],
        "protection": 0,
    }

    for armour_part in knight["armour"]:
        prepared_knight["protection"] += armour_part["protection"]

    prepared_knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]

        prepared_knight["hp"] += potion_effect.get("hp", 0)
        prepared_knight["power"] += potion_effect.get("power", 0)
        prepared_knight["protection"] += potion_effect.get("protection", 0)

    return prepared_knight


def fight(knight_1: PreparedKnight, knight_2: PreparedKnight) -> None:
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]

    if knight_1["hp"] <= 0:
        knight_1["hp"] = 0

    if knight_2["hp"] <= 0:
        knight_2["hp"] = 0


def battle(knights_config: dict[str, KnightConfig]) -> dict[str, int]:
    lancelot = prepare_knight(knights_config["lancelot"])
    arthur = prepare_knight(knights_config["arthur"])
    mordred = prepare_knight(knights_config["mordred"])
    red_knight = prepare_knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
