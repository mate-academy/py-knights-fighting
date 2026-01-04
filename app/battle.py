from app.knights import Knights


def fell_check(knight: Knights) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def fight(first_knight: Knights, second_knight: Knights) -> None:

    first_knight.fight_preparing()
    second_knight.fight_preparing()
    # print(first_knight.power, first_knight.hp, first_knight.protection)
    # print(second_knight.power, second_knight.hp, second_knight.protection)

    first_knight.hp -= max(0, second_knight.power - first_knight.protection)
    second_knight.hp -= max(0, first_knight.power - second_knight.protection)

    fell_check(first_knight)
    fell_check(second_knight)
