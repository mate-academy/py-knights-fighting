def perform_battle(knights):
    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    lancelot_protection = lancelot.apply_armour()
    arthur_protection = arthur.apply_armour()

    lancelot_power = lancelot.apply_weapon()
    arthur_power = arthur.apply_weapon()
    mordred_power = mordred.apply_weapon()
    red_knight_power = red_knight.apply_weapon()

    while lancelot.hp > 0 and mordred.hp > 0:
        lancelot.hp -= mordred_power - lancelot_protection
        mordred.hp -= lancelot_power - mordred.apply_armour()

    if lancelot.hp <= 0 and mordred.hp <= 0:
        return "Draw"
    elif lancelot.hp <= 0:
        return "Mordred wins"
    else:
        return "Lancelot wins"
