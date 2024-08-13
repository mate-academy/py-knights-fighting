from typing import Dict
from app.knight import Knight
from app.battle import Battle

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 50,
        "hp": 80,
        "armour": [{"part": "helmet", "protection": 10}],
        "weapon": {"name": "Sword", "power": 30},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 5}
        ],
        "weapon": {"name": "Sword", "power": 25},
        "potion": {"name": "Blessing", "effect": {"hp": 20, "power": 10}},
    },
    "mordred": {
        "name": "Mordred",
        "power": 55,
        "hp": 85,
        "armour": [{"part": "shield", "protection": 30}],
        "weapon": {"name": "Axe", "power": 35},
        "potion": None,
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {"name": "Blessing", "effect": {"hp": 10, "power": 5}},
    },
}


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    knights = {
        name: Knight(**config)
        for name, config in knights_config.items()
    }
    results = {}

    # Lancelot vs Mordred
    battle_instance = Battle(knights["lancelot"], knights["mordred"])
    result = battle_instance.fight()
    results["Lancelot"] = result[knights["lancelot"].name]
    results["Mordred"] = result[knights["mordred"].name]

    # Arthur vs Red Knight
    battle_instance = Battle(knights["arthur"], knights["red_knight"])
    result = battle_instance.fight()
    results["Arthur"] = result[knights["arthur"].name]
    results["Red Knight"] = result[knights["red_knight"].name]

    return results


def main() -> None:
    result = battle(KNIGHTS)
    print(result)


if __name__ == "__main__":
    main()
