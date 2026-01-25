from app.Knights.knights import Knight

# damage counting


def calc_damage(power: int, protection: int) -> int:
    return max(0, power - protection)

# duel takes two knights and call "calc_damage"


def duel(couple: tuple["Knight", "Knight"]) -> dict[str, int]:
    duel_result = {}
    # Proceed with the duel only if both knights in the pair are present
    if couple[0] is not None and couple[1] is not None:
        for idx in range(len(couple)):
            hp = couple[idx].hp
            hp -= calc_damage(
                couple[(idx + 1) % 2].power,
                couple[idx].protection
            )
            duel_result.update({couple[idx].name: max(0, hp)})
    return duel_result

# battle itterates through the list of couples
# and call "duel" func for each couple


def battle(knights: dict) -> dict[str, int]:
    battle_result = {}
    pairs = Knight.build_knight_couples_from_cfg(knights)
    for couple in pairs:
        battle_result.update(duel(couple))
    return battle_result
