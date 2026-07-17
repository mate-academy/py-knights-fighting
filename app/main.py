from app.knights.knight import Knight
from app.knights.battle import fight


def battle(knights_config: dict) -> dict:
    knights_dict = {}
    for knight_data in knights_config.values():
        knight = Knight(
            knight_data["name"],
            knight_data["power"],
            knight_data["hp"],
            knight_data["armour"],
            knight_data["weapon"],
            knight_data.get("potion"))
        knights_dict[knight_data["name"]] = knight

    knights = list(knights_dict.values())
    fight(knights[0], knights[2])
    fight(knights[1], knights[3])
    return {knight.name: knight.hp for knight in knights_dict.values()}
gi