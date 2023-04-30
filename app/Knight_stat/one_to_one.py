def one_to_one(knights: list[tuple]) -> list[int]:
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
    return [lancelot_hp_after,
            arthur_hp_after,
            mordred_hp_after,
            red_knight_hp_after]
