from app.person.knight import Knight


def game(person: Knight, other: Knight) -> None:
    person.hp -= other.power - person.protection
    other.hp -= person.power - other.protection
    defeat(person)
    defeat(other)
    return person.hp, other.hp


def defeat(person: Knight) -> None:
    if person.hp <= 0:
        person.hp = 0
