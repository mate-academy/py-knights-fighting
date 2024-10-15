from app.data import KNIGHTS
from app.knight import Knight


def battle_between(knight1: Knight, knight2: Knight) -> None:
    knight1 -= knight2 - knight1
    knight2 -= knight1 - knight2


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {name: Knight(value) for name, value in knights_config.items()}
    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    battle_between(knights["lancelot"], knights["mordred"])
    # 2 Arthur vs Red Knight:
    battle_between(knights["arthur"], knights["red_knight"])
    # Return battle results:
    return {value.name: value.hp for value in knights.values()}


print(battle(KNIGHTS))
