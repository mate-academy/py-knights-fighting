from app.knights_data import KNIGHTS
from app.knight_class import Knight


def check_hp(knight: Knight) -> None:
    """If hp less than 0 hp equals 0"""
    if knight.hp <= 0:
        knight.hp = 0


def resolve_fight(knight_1: Knight, knight_2: KNIGHTS) -> None:
    """Count fight result"""
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    check_hp(knight_1)
    check_hp(knight_2)


def battle(knights_config: dict) -> dict:

    # Knights
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Battle
    resolve_fight(lancelot, mordred)
    resolve_fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
