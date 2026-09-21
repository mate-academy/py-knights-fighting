from app.knight import Knight
from app.fight import Fight
from app.constants import KNIGHTS


def build_knight(knight: dict) -> Knight:
    data = Knight(knight["name"], knight["power"], knight["hp"])
    data.battle_preparation(
        knight["armour"],
        knight["weapon"],
        knight["potion"],
    )
    return data


def battle(knights_config: dict) -> dict:
    knights = {}

    for key, value in knights_config.items():
        knights[key] = build_knight(value)

    Fight.fight(knights["lancelot"], knights["mordred"])
    Fight.fight(knights["red_knight"], knights["arthur"])

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
