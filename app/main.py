from app.Knight_stat.calc_knight_stat import Lancelot_stat, Mordred_stat, Arthur_stat, Red_knight_stat
from app.Knight_stat.calc_knight_stat import Lancelot_, Mordred_, Arthur_, Red_knight_

KNIGHTS = {Lancelot_stat, Mordred_stat, Arthur_stat, Red_knight_stat}


def battle(solution: set[tuple]):
    lancelot_hp_after = Lancelot_stat[0] - Mordred_stat[1]
    mordred_hp_after = Mordred_stat[0] - Lancelot_stat[1]
    if lancelot_hp_after <= 0:
        lancelot_hp_after += abs(lancelot_hp_after)
    if mordred_hp_after <= 0:
        mordred_hp_after += abs(mordred_hp_after)

    arthur_hp_after = Arthur_stat[0] - Red_knight_stat[1]
    red_knight_hp_after = Red_knight_stat[0] - Arthur_stat[1]
    if arthur_hp_after <= 0:
        arthur_hp_after += abs(arthur_hp_after)
    if red_knight_hp_after <= 0:
        red_knight_hp_after += abs(red_knight_hp_after)

    return {
        Lancelot_["name"]: lancelot_hp_after,
        Arthur_["name"]: arthur_hp_after,
        Mordred_["name"]: mordred_hp_after,
        Red_knight_["name"]: red_knight_hp_after,
    }


print(battle(KNIGHTS))
