from app.program_data.knight import Knight


def less_null(number: int) -> int:
    return 0 if number <= 0 else number


def duel(hero_1: Knight, hero_2: Knight) -> None:
    [hero.preparation_for_battle() for hero in (hero_1, hero_2)]

    hero_1.hp -= hero_2.power - hero_1.protection
    hero_1.hp = less_null(hero_1.hp)

    hero_2.hp -= hero_1.power - hero_2.protection
    hero_2.hp = less_null(hero_2.hp)
