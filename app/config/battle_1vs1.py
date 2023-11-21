from app.config.knight import Knight


def battle_1vs1(knight_1: str, knight_2: str) -> None:
    pers = Knight.persons
    pers[knight_1].hp -= pers[knight_2].power - pers[knight_1].protection
    pers[knight_2].hp -= pers[knight_1].power - pers[knight_2].protection
    pers[knight_1].hp = max(0, pers[knight_1].hp)
    pers[knight_2].hp = max(0, pers[knight_2].hp)
