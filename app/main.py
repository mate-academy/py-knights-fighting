from app.knight.knight import Knight
from app.battle.fight import fight


KNIGHTS = [
    Knight(
        "Lancelot",
        35, 100,
        [], {"name": "Metal Sword", "power": 50}, None),
    Knight("Arthur", 45, 75, [
        {"part": "helmet", "protection": 15},
        {"part": "breastplate", "protection": 20},
        {"part": "boots", "protection": 10}
    ], {"name": "Two-handed Sword", "power": 55}, None),
    Knight("Mordred", 30, 90, [
        {"part": "breastplate", "protection": 15},
        {"part": "boots", "protection": 10}
    ], {
        "name": "Poisoned Sword", "power": 60},
        {"name": "Berserk",
         "effect": {
             "power": 15, "hp": -5, "protection": 10}}),
    Knight("Red Knight", 40, 70, [
        {"part": "breastplate", "protection": 25}
    ], {"name": "Sword", "power": 45}, {"name": "Blessing",
                                        "effect": {
                                            "hp": 10, "power": 5}})
]


def battle(knights_config: list) -> dict:
    knights = [knight.prepare_knight() for knight in knights_config]
    battle_results = fight(knights[0], knights[2])
    battle_results.update(fight(knights[1], knights[3]))
    return battle_results


print(battle(KNIGHTS))
