from app.knight import Knights


def battle(knights: dict) -> dict:

    lancelot, arthur, mordred, red_knight = [
        Knights(knight) for knight in knights.values()
    ]

    knights_list = [lancelot, arthur, mordred, red_knight]

    for knight in knights_list:
        knight.preparation()

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {knight.name: knight.hp for knight in knights_list}
