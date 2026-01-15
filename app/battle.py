from app.knights.knight import Knight


def check_loser(fighter_hp: int) -> int:
    if fighter_hp <= 0:
        fighter_hp = 0
    return fighter_hp


def fight(first_fighter: Knight, second_fighter: Knight) -> None:

    first_fighter.hp -= second_fighter.power - first_fighter.protection
    second_fighter.hp -= first_fighter.power - second_fighter.protection

    first_fighter.hp = check_loser(first_fighter.hp)
    second_fighter.hp = check_loser(second_fighter.hp)
