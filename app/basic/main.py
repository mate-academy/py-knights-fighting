from app.stats.knight import Knight


def battle(knight1: Knight, knight2: Knight):
    while knight1.hp > 0 and knight2.hp > 0:
        knight2.hp -= knight1.power - knight2.protection
        knight1.hp -= knight2.power - knight1.protection

        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0

    return {knight1.name: knight1.hp, knight2.name: knight2.hp}


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
        "name": "Artur",
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
