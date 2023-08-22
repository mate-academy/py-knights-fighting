from app.battle_preparations.apply_potion import apply_potion


def battle(knights_dict: dict) -> dict:

    knights_list = apply_potion(knights_dict)

    [lancelot, arthur, mordred, red_knight] = \
        [knights_list[0], knights_list[1], knights_list[2], knights_list[3]]

    rounds = [(lancelot, mordred),
              (arthur, red_knight),
              (mordred, lancelot),
              (red_knight, arthur)]

    for knight, opponent in rounds:
        knight.hp -= opponent.power - knight.protection

    for knight in knights_list:
        if knight.hp <= 0:
            knight.hp = 0

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in knights_list
    }
