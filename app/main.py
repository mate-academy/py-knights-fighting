from app.knights import Knight


def battle(knight: dict) -> dict:
    lancelot = Knight(knight["lancelot"])
    mordred = Knight(knight["mordred"])
    arthur = Knight(knight["arthur"])
    red_knight = Knight(knight["red_knight"])

    lancelot.battle_knight(mordred)
    arthur.battle_knight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,

    }
