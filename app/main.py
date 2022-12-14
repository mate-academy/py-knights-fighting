from app.pkg.fighting import fighting
from app.pkg.knight_config import KNIGHTS
from app.pkg.preparations import preparations


def battle(knights: dict) -> dict:
    knights_dict = preparations(knights)

    # 1 Lancelot vs Mordred:
    fighting("lancelot", "mordred", knights_dict)

    # 2 Arthur vs Red Knight:
    fighting("arthur", "red_knight", knights_dict)

    return {knights_dict[name].name: knights_dict[name].hp
            for name in knights_dict}


print(battle(KNIGHTS))
