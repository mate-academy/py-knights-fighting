from app.data import KNIGHTS
from app.knight import Knight

battle_table = [
    ("lancelot", "mordred"),
    ("arthur", "red_knight")
]


def battle_between(knight1: Knight, knight2: Knight) -> None:
    knight1.fight(knight2.reduce_power(knight1))
    knight2.fight(knight1.reduce_power(knight2))


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {name: Knight(value) for name, value in knights_config.items()}
    for knight in knights.values():
        knight.preparation()
    # -------------------------------------------------------------------------------
    # BATTLE:
    for knight1, knight2 in battle_table:
        battle_between(knights[knight1], knights[knight2])
    # Return battle results:
    return {value.name: value.hp for value in knights.values()}


print(battle(KNIGHTS))
