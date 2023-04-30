from app.Knight_stat.calc_knight_stat import knight_stat


def battle(knights_main: dict) -> dict:

    knights = []
    for knight in knights_main.values():
        knights.append(knight_stat(knight))
    lancelot_hp_after = knights[0][0] - knights[2][1]
    mordred_hp_after = knights[2][0] - knights[0][1]
    if lancelot_hp_after <= 0:
        lancelot_hp_after += abs(lancelot_hp_after)
    if mordred_hp_after <= 0:
        mordred_hp_after += abs(mordred_hp_after)

    arthur_hp_after = knights[1][0] - knights[3][1]
    red_knight_hp_after = knights[3][0] - knights[1][1]
    if arthur_hp_after <= 0:
        arthur_hp_after += abs(arthur_hp_after)
    if red_knight_hp_after <= 0:
        red_knight_hp_after += abs(red_knight_hp_after)
    knights_hp_after = [lancelot_hp_after,
                        arthur_hp_after,
                        mordred_hp_after,
                        red_knight_hp_after]
    return {knights_main[knight]["name"]: knights_hp_after[number]
            for number, knight in enumerate(knights_main)}
