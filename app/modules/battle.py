from app.modules.knights import Knight


def battle(knights_dict: dict) -> dict:

    Knight.make_knight(knights_dict)
    knight = Knight.knights_list

    result_dict = {}

    for i in range(0,len(knight), 2):

        knight1 = knight[i]
        knight2 = knight[i + 1]

        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0

        result_dict.update({
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        })
    return result_dict
