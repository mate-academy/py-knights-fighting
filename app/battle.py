from knight import Knight
from main import KNIGHTS


lancelot = Knight("lancelot", KNIGHTS)
arthur = Knight("arthur", KNIGHTS)
mordred = Knight("mordred", KNIGHTS)
red_knight = Knight("red_knight", KNIGHTS)


def battle_preparation(knight: Knight) -> None:
    """Function prepare knight for a battle"""
    knight.get_armour()
    knight.get_weapon()
    knight.get_potion()


def duel(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection


def check_if_fell(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def battle_results(knights: list[Knight]) -> dict:
    return {knight.real_name: knight.hp for knight in knights}


battle_preparation(lancelot)
battle_preparation(arthur)
battle_preparation(mordred)
battle_preparation(red_knight)

duel(lancelot, mordred)
duel(arthur, red_knight)

check_if_fell(lancelot)
check_if_fell(arthur)
check_if_fell(mordred)
check_if_fell(red_knight)

print(battle_results([lancelot, arthur, mordred, red_knight]))


# 1 Lancelot vs Mordred:
# 2 Arthur vs Red Knight:
# Return battle results:
