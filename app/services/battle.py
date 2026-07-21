from app.models.knight import Knight


def fight(first: Knight, second: Knight) -> dict:
    first.take_damage(second.power)
    second.take_damage(first.power)

    return {
        first.name: first.hp,
        second.name: second.hp,
    }
