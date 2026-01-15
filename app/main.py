from app.knight import Knight
from app.knights import KNIGHTS, knights_battle


def create_knight(data: dict) -> Knight:
    return Knight(**data)


def battle(knights_config: dict[dict]) -> dict:
    knights = {}

    for knight_name, knight_data in knights_config.items():
        knights[knight_name] = create_knight(knight_data)

    knights_battle(knights["lancelot"], knights["mordred"])
    knights_battle(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
