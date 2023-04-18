from app.stats.knight import Knight


def knight_fight(knight1: Knight, knight2: Knight) -> dict:
    knight1.apply_potion()
    knight2.apply_potion()
    knight2.apply_armour()
    knight1.apply_armour()
    knight1.apply_weapon()
    knight2.apply_weapon()

    knight2.hp -= knight1.power - knight2.protection
    knight1.hp -= knight2.power - knight1.protection
    if knight1.hp < 0:
        knight1.hp = 0
    if knight2.hp < 0:
        knight2.hp = 0
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}


def battle(knight_config: dict) -> dict:
    dict_with_knight = {}
    for knight_name, attributes in knight_config.items():
        dict_with_knight[knight_name] = Knight(**attributes)
    knight_fight(dict_with_knight["lancelot"], dict_with_knight["mordred"])
    knight_fight(dict_with_knight["arthur"], dict_with_knight["red_knight"])
    return {
        "Lancelot": dict_with_knight.get("lancelot").hp,
        "Artur": dict_with_knight.get("arthur").hp,
        "Mordred": dict_with_knight.get("mordred").hp,
        "Red Knight": dict_with_knight.get("red_knight").hp,
    }


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
battle(KNIGHTS)
