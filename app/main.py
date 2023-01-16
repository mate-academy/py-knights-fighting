from app.knights_config import KNIGHTS
from app.knight_crearing import create_knight


def check_hp(hp: int) -> int:
    if hp <= 0:
        return 0
    return hp


def battle(knights: dict) -> dict:
    list_of_knights = []
    for knight in knights:
        knight_ = create_knight(knights[knight])
        knight_.apply_armour(knights[knight])
        knight_.apply_weapon(knights[knight])
        knight_.apply_potion(knights[knight]["potion"])
        list_of_knights.append(knight_)

    list_of_knights[0].hp -= \
        list_of_knights[2].power - list_of_knights[0].protection
    list_of_knights[2].hp -= \
        list_of_knights[0].power - list_of_knights[2].protection

    list_of_knights[1].hp -= \
        list_of_knights[3].power - list_of_knights[1].protection
    list_of_knights[3].hp -= \
        list_of_knights[1].power - list_of_knights[3].protection

    for knight in list_of_knights:
        knight.hp = check_hp(knight.hp)

    return {
        list_of_knights[0].name: list_of_knights[0].hp,
        list_of_knights[1].name: list_of_knights[1].hp,
        list_of_knights[2].name: list_of_knights[2].hp,
        list_of_knights[3].name: list_of_knights[3].hp,
    }


print(battle(KNIGHTS))
