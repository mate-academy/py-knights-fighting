from app.fighters.knight import Knight


def knights_preparation(knights: list[Knight]) -> list[Knight]:
    return [knight.preparing_for_battle() for knight in knights]


def start_battle(first_knight: str, second_knight: str,
                 all_knights: list[Knight]) -> list[Knight]:
    first_battler = None
    # first battler index
    f_b_i = 0
    second_battler = None
    # second battler index
    s_b_i = 0

    # select required knights
    for i, knight in enumerate(all_knights):
        if first_knight == knight.name:
            first_battler = knight
            f_b_i = i
        if second_knight == knight.name:
            second_battler = knight
            s_b_i = i

    # start of battle
    first_battler.battle_with(second_battler)
    second_battler.battle_with(first_battler)

    first_battler.check_if_defeated()
    second_battler.check_if_defeated()

    all_knights[f_b_i] = first_battler
    all_knights[s_b_i] = second_battler
    return all_knights
