from app.knights import Knight


def fight(fighter_first: Knight, fighter_second: Knight) -> None:
    fighter_first.hp -= fighter_second.power - fighter_first.protection
    if fighter_first.hp <= 0:
        fighter_first.hp = 0
    fighter_second.hp -= fighter_first.power - fighter_second.protection
    if fighter_second.hp <= 0:
        fighter_second.hp = 0
