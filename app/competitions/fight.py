from app.characters.knights import Character


def fight(first_fighter: Character, second_fighter: Character) -> None:
    first_fighter.hp -= second_fighter.power - first_fighter.protection
    second_fighter.hp -= first_fighter.power - second_fighter.protection

    first_fighter.is_fell_in_battle()
    second_fighter.is_fell_in_battle()
