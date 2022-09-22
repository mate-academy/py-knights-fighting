from app.heroes.fighter import Hero


def brawl(first_fighter: Hero, second_fighter: Hero) -> None:
    first_fighter.hp -= second_fighter.power - first_fighter.protection
    if first_fighter.hp <= 0:
        first_fighter.hp = 0
    second_fighter.hp -= first_fighter.power - second_fighter.protection
    if second_fighter.hp <= 0:
        second_fighter.hp = 0
