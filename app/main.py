from app.knight import Knight
from app.battle import Battle


lancelot = Knight(
    "Lancelot",
    35,
    100,
    [],
    {"name": "Metal Sword", "power": 50},
    None,
    0)

arthur = Knight(
    "Arthur",
    45,
    75,
    [{"part": "helmet", "protection": 15},
     {"part": "breastplate", "protection": 20},
     {"part": "boots", "protection": 10}],
    {"name": "Two-handed Sword", "power": 55},
    None,
    0)

mordred = Knight(
    "Mordred",
    30,
    90,
    [{"part": "breastplate", "protection": 15},
     {"part": "boots", "protection": 10}],
    {"name": "Poisoned Sword", "power": 60},
    {"name": "Berserk",
     "effect": {"power": +15, "hp": -5, "protection": +10}},
    0)

red_knight = Knight(
    "red_knight",
    40,
    70,
    [{"part": "breastplate", "protection": 25}],
    {"name": "Sword", "power": 45},
    {"name": "Blessing",
     "effect": {"hp": +10, "power": +5}},
    0)

KNIGHTS = [lancelot, arthur, mordred, red_knight]


def battle(knights_config: list) -> dict:
    for knight in knights_config:
        Knight.apply_armour(knight)
        Knight.apply_weapon(knight)
        Knight.apply_potion(knight)

    Battle.battle(lancelot, arthur)
    Battle.battle(mordred, red_knight)

    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}


print(battle(KNIGHTS))
