from app.config.knight import Knight


def battle_1vs1(knight_1: str, knight_2: str) -> None:
    first_knight, second_knight = (Knight.persons[knight_1],
                                   Knight.persons[knight_2])
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    first_knight.hp = max(0, first_knight.hp)
    second_knight.hp = max(0, second_knight.hp)
