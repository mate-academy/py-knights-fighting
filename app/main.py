from app.declarations.battle_configs import Knights
from app.knight.knight import Knight


def battle(knight_configs: dict = Knights) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight(knight_configs["lancelot"])
    arthur = Knight(knight_configs["arthur"])
    mordred = Knight(knight_configs["mordred"])
    red_knight = Knight(knight_configs["red_knight"])

    # BATTLE:
    mordred.attack(lancelot)
    lancelot.attack(mordred)

    red_knight.attack(arthur)
    arthur.attack(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle())
