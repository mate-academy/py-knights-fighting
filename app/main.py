from app.knight_class import Knight
from app.knights_info import KNIGHTS


def duel(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if first_knight.hp <= 0:
        first_knight.hp = 0
    if second_knight.hp <= 0:
        second_knight.hp = 0


def battle(knights_config: dict) -> dict:
    knights = {
        member: Knight(knights_config[member]) for member in knights_config
    }
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])
    return {
        knights[member].name: knights[member].hp for member in knights
    }


print(battle(KNIGHTS))
