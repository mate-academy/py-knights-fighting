from app.warrior import Knight


def battle_knights(list_knight: list[Knight]) -> dict:
    result_of_battles = {}
    knight = 2
    for i in range(len(list_knight)):
        result = list_knight[knight].power - list_knight[i].protection
        list_knight[i].hp -= result
        if list_knight[i].hp <= 0:
            list_knight[i].hp = 0
        result_of_battles[list_knight[i].name] = list_knight[i].hp
        knight += 1
        knight %= len(list_knight)
    return result_of_battles
