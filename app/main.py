from app.knight_class import Knight
from app.knights_info import KNIGHTS


def duel(member_1: Knight, member_2: Knight) -> None:
    member_1.hp -= member_2.power - member_1.protection
    member_2.hp -= member_1.power - member_2.protection

    if member_1.hp <= 0:
        member_1.hp = 0
    if member_2.hp <= 0:
        member_2.hp = 0


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
