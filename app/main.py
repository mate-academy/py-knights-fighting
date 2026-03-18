from app.data.knights import KNIGHTS
from app.models.knight_class import Knight
from app.simulations.prepare import prepare_knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])
    prepare_knight(lancelot)
    prepare_knight(arthur)
    prepare_knight(mordred)
    prepare_knight(red_knight)

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
