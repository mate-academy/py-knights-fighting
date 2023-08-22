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
        knight.hp = 0 if knight.hp < 0 else knight.hp

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in knights_list
    }
