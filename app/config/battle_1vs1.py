from app.config.knights import Knights


def battle_1vs1(knight_1: str, knight_2: str) -> None:
    pers = Knights.persons
    pers[knight_1].hp -= pers[knight_2].power - pers[knight_1].protection
    pers[knight_2].hp -= pers[knight_1].power - pers[knight_2].protection
    if pers[knight_1].hp <= 0:
        pers[knight_1].hp = 0
    if pers[knight_2].hp <= 0:
        pers[knight_2].hp = 0
