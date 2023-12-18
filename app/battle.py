from app.knight import Knights


def battle(knight: dict) -> dict:
    lancelot = Knights(knight["lancelot"])
    arthur = Knights(knight["arthur"])
    mordred = Knights(knight["mordred"])
    red_knight = Knights(knight["red_knight"])

    knights = (lancelot, arthur, mordred, red_knight)
    for knight in knights:
        knight.preparation()

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {knight.name: knight.hp for knight in knights}
