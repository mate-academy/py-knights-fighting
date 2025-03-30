from app.knight import Knight
from app.battle import Battle

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
        "armour": [{
            "part": "breastplate",
            "protection": 15}, {"part": "boots", "protection": 10}],
        "weapon": {"name": "Poisoned Sword", "power": 60},
        "potion": {
            "name": "Berserk",
            "effect": {"power": +15,
                       "hp": -5, "protection": +10}},
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


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    result_lancelot_mordred = Battle(lancelot, mordred).execute()
    result_arthur_red_knight = Battle(arthur, red_knight).execute()

    return {
        lancelot.name: result_lancelot_mordred[lancelot.name],
        arthur.name: result_arthur_red_knight[arthur.name],
        mordred.name: result_lancelot_mordred[mordred.name],
        red_knight.name: result_arthur_red_knight[red_knight.name],
    }
