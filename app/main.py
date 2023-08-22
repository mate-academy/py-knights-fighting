from app.battle_preparations.apply_potion import apply_potion


def battle(knights_dict: dict) -> dict:

    knights_list = apply_potion(knights_dict)

    for index in range(2):
        knights_list[index].hp -= (knights_list[index + 2].power
                                   - knights_list[index].protection)
        knights_list[index + 2].hp -= (knights_list[index].power
                                       - knights_list[index + 2].protection)

    for knight in knights_list:
        if knight.hp <= 0:
            knight.hp = 0

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in knights_list
    }
