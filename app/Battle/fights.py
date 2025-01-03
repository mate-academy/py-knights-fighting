from app.Preparation.Knights import Knight


def fight(fighter_1: Knight, fighter_2: Knight) -> None:
    fighter_1.hp -= (fighter_2.power - fighter_1.armour)
    fighter_2.hp -= (fighter_1.power - fighter_2.armour)

    if fighter_1.hp <= 0:
        fighter_1.hp = 0

    if fighter_2.hp <= 0:
        fighter_2.hp = 0
