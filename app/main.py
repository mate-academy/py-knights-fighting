from app.battle_preparations.apply_potion import apply_potion


def battle(knights_dict: dict) -> dict:

    knights_list = apply_potion(knights_dict)

    [lancelot, arthur, mordred, red_knight] = \
        [knights_list[0], knights_list[1], knights_list[2], knights_list[3]]
    knight = [lancelot, arthur, mordred, red_knight]
    opponent = [mordred, red_knight, lancelot, arthur]

    for index in range(4):
        knight[index].hp -= opponent[index].power - knight[index].protection

    for knight in knights_list:
        if knight.hp <= 0:
            knight.hp = 0

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in knights_list
    }
