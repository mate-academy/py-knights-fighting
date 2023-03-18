def round_n(list_of_fighters: list, order_of_battle: list) -> dict:
    for fight in order_of_battle:
        for losses in range(len(fight)):
            iit = fight[losses] - 1
            jit = fight[1 - losses] - 1
            list_of_fighters[iit].hp -=\
                list_of_fighters[jit].power -\
                list_of_fighters[iit].protection
            if list_of_fighters[iit].hp < 0:
                list_of_fighters[iit].hp = 0

    return {
        knight_result.noble_name: knight_result.hp
        for knight_result in list_of_fighters
    }
