from app.Knight.knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knight_key=knights["lancelot"])
    arthur = Knight(knight_key=knights["arthur"])
    mordred = Knight(knight_key=knights["mordred"])
    red_knight = Knight(knight_key=knights["red_knight"])
    lancelot.fight(mordred)
    arthur.fight(red_knight)
    return {lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}
