from app.knights.knights import init_knights, battle_between_knights, make_pair
from app.knights.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = init_knights(knights_config)
    battle_between_knights(make_pair(knights))
    return {knight.name: knight.hp for knight in knights}


print(battle(KNIGHTS))
