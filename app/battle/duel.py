from app.Challengers.Knight import Hero


def fight(first_fighter: Hero, second_fighter: Hero) -> None:
    first_fighter_damage = first_fighter.power - second_fighter.armour
    second_fighter_damage = second_fighter.power - first_fighter.armour
    first_fighter.hp = max(0, first_fighter.hp - second_fighter_damage)
    second_fighter.hp = max(0, second_fighter.hp - first_fighter_damage)
