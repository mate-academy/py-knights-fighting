from typing import Dict, Any


KNIGHTS: Dict[str, Dict[str, Any]] = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {
            "name": "Berserk",
            "effect": {"power": +15, "hp": -5, "protection": +10},
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [{"part": "breastplate", "protection": 25}],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {"hp": +10, "power": +5},
        },
    },
}


def prepare_knight(knight: Dict[str, Any]) -> None:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"]:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value


def fight(knight1: Dict[str, Any], knight2: Dict[str, Any]) -> None:
    damage1 = max(0, knight2["power"] - knight1["protection"])
    damage2 = max(0, knight1["power"] - knight2["protection"])
    knight1["hp"] = max(0, knight1["hp"] - damage1)
    knight2["hp"] = max(0, knight2["hp"] - damage2)


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    knights = {k: v.copy() for k, v in knights_config.items()}
    for knight in knights.values():
        prepare_knight(knight)
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])
    return {k["name"]: k["hp"] for k in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
