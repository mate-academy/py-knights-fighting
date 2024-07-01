from app.warrior import Knight


def battle_knights(list_knight: list[Knight]) -> dict:
    result_of_battles = {}
    list_knight[0].hp -= list_knight[2].power - list_knight[0].protection
    if list_knight[0].hp <= 0:
        list_knight[0].hp = 0
    result_of_battles[list_knight[0].name] = list_knight[0].hp

    list_knight[1].hp -= list_knight[3].power - list_knight[1].protection
    if list_knight[1].hp <= 0:
        list_knight[1].hp = 0
    result_of_battles[list_knight[1].name] = list_knight[1].hp

    list_knight[2].hp -= list_knight[0].power - list_knight[2].protection
    if list_knight[2].hp <= 0:
        list_knight[2].hp = 0
    result_of_battles[list_knight[2].name] = list_knight[2].hp

    list_knight[3].hp -= list_knight[1].power - list_knight[3].protection
    if list_knight[3].hp <= 0:
        list_knight[3].hp = 0
    result_of_battles[list_knight[3].name] = list_knight[3].hp
    return result_of_battles
