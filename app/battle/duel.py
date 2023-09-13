from app.Challengers.Knight import Hero


def fight(first_fighter: Hero, second_fighter: Hero) -> None:
    first_fighter.hp -= second_fighter.power - first_fighter.armour
    second_fighter.hp -= first_fighter.power - second_fighter.armour
