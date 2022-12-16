from app.pkg.fighting import fighting
from app.pkg.knight_config import KNIGHTS
from app.pkg.preparations import preparations


def battle(knights: dict) -> dict:
    knights_dict = preparations(knights)

    battle_distribution = {"lancelot": "mordred", "arthur": "red_knight"}
    for first, second in battle_distribution.items():
        fighting(first, second, knights_dict)

    return {knights_dict[name].name: knights_dict[name].hp
            for name in knights_dict}


print(battle(KNIGHTS))
