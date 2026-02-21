from copy import deepcopy
from app.knights.models import Knight

KNIGHTS = {
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
        "potion": {"name": "Blessing", "effect": {"hp": +10, "power": +5}},
    },
}

KNIGHT_ORDER = ["lancelot", "mordred", "arthur", "red_knight"]


def _fight(first: dict, second: dict) -> tuple[int, int]:
    damage_to_first = max(0, second["power"] - first["protection"])
    damage_to_second = max(0, first["power"] - second["protection"])
    new_first_hp = max(0, first["hp"] - damage_to_first)
    new_second_hp = max(0, second["hp"] - damage_to_second)
    return new_first_hp, new_second_hp


def battle(knights_config: dict) -> dict[str, int]:
    knights = deepcopy(knights_config)
    created_knights = {
        name: Knight(**knights[name])
        for name in KNIGHT_ORDER
    }
    stats = {
        name: knight.prepare_stats()
        for name, knight in created_knights.items()
    }
    assert all(isinstance(s, dict) for s in stats.values())
    assert all(k in stats["lancelot"] for k in ("hp", "power", "protection"))
    l_hp, m_hp = _fight(stats["lancelot"], stats["mordred"])
    a_hp, r_hp = _fight(stats["arthur"], stats["red_knight"])
    return {
        created_knights["lancelot"].name: l_hp,
        created_knights["arthur"].name: a_hp,
        created_knights["mordred"].name: m_hp,
        created_knights["red_knight"].name: r_hp,
    }
