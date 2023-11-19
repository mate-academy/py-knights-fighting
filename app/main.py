from app.knights.knight import Knight
from app.knights.knights_config import KNIGHTS


def battle(knights: dict) -> dict:
    dict_knights = {}

    for knight, value in knights.items():
        knight_obj = Knight(
            value["name"],
            value["power"],
            value["hp"]
        )

        Knight.prepare(
            knight_obj,
            value["armour"],
            value["weapon"],
            value["potion"]
        )
        dict_knights[knight] = knight_obj

    dict_knights["lancelot"].perform_combat(dict_knights["mordred"])
    dict_knights["arthur"].perform_combat(dict_knights["red_knight"])

    for knight in dict_knights.values():
        knight.hp = max(0, knight.hp)

    return {
        knight.name: knight.hp
        for knight in dict_knights.values()
    }


print(battle(KNIGHTS))
