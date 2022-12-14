from app.pkg.fighting import fighting
from app.pkg.knight_config import KNIGHTS
from app.pkg.preparations import preparations


def battle(knights: dict) -> dict:
    preparations(knights)

    # 1 Lancelot vs Mordred:
    fighting("lancelot", "mordred", knights)

    # 2 Arthur vs Red Knight:
    fighting("arthur", "red_knight", knights)

    return {knights[name]["name"]: knights[name]["hp"] for name in knights}


print(battle(KNIGHTS))
