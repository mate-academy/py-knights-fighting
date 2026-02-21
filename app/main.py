from copy import deepcopy
from app.knights.models import Knight


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
            {"part": "helmet", "protection": 15},
            {"part": "breastplate", "protection": 20},
            {"part": "boots", "protection": 10},
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
            {"part": "breastplate", "protection": 15},
            {"part": "boots", "protection": 10},
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
            {"part": "breastplate", "protection": 25},
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


def _create_knight(conf: dict) -> Knight:
    return Knight(
        conf["name"],
        conf["hp"],
        conf["power"],
        conf.get("armour"),
        conf.get("weapon"),
        conf.get("potion"),
    )


def _fight(a: dict, b: dict) -> tuple[int, int]:
    dmg_to_a = max(0, b["power"] - a["protection"])
    dmg_to_b = max(0, a["power"] - b["protection"])
    new_a = max(0, a["hp"] - dmg_to_a)
    new_b = max(0, b["hp"] - dmg_to_b)
    return new_a, new_b


def battle(knightsConfig: dict) -> dict:
    k = deepcopy(knightsConfig)

    lancelot = _create_knight(k["lancelot"])
    mordred = _create_knight(k["mordred"])
    arthur = _create_knight(k["arthur"])
    red = _create_knight(k["red_knight"])

    l_stats = lancelot.prepare_stats()
    m_stats = mordred.prepare_stats()
    a_stats = arthur.prepare_stats()
    r_stats = red.prepare_stats()

    l_hp, m_hp = _fight(l_stats, m_stats)
    a_hp, r_hp = _fight(a_stats, r_stats)

    return {
        lancelot.name: l_hp,
        arthur.name: a_hp,
        mordred.name: m_hp,
        red.name: r_hp,
    }


print(battle(KNIGHTS))