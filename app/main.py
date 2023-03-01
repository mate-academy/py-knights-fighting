from app.knights_config import KNIGHTS
from app.knight_crearing import create_knight, Knight


def check_hp(hp: int) -> int:
    if hp <= 0:
        return 0
    return hp


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection


def battle(knights: dict) -> dict:
    dict_of_knights = {}
    for knight in knights:
        knight_ = create_knight(knights[knight])
        knight_.apply_armour(knights[knight])
        knight_.apply_weapon(knights[knight])
        knight_.apply_potion(knights[knight]["potion"])
        dict_of_knights[knight] = knight_

    fight(dict_of_knights["lancelot"], dict_of_knights["mordred"])
    fight(dict_of_knights["arthur"], dict_of_knights["red_knight"])

    for knight in dict_of_knights:
        dict_of_knights[knight].hp = check_hp(dict_of_knights[knight].hp)

    return {
        dict_of_knights["lancelot"].name: dict_of_knights["lancelot"].hp,
        dict_of_knights["arthur"].name: dict_of_knights["arthur"].hp,
        dict_of_knights["mordred"].name: dict_of_knights["mordred"].hp,
        dict_of_knights["red_knight"].name: dict_of_knights["red_knight"].hp
    }


battle(KNIGHTS)
