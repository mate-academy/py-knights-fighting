def check_hp(hp: int) -> int:
    # check if someone fell in battle
    if hp <= 0:
        hp = 0
    return hp
