from app.components.knights import KNIGHTS
from app.service.make_knights import make_knights


def battle(knights: dict) -> dict:
    new_knights = make_knights(knights)

    lancelot = new_knights["lancelot"]
    arthur = new_knights["arthur"]
    mordred = new_knights["mordred"]
    red_knight = new_knights["red_knight"]

    mordred.fight(lancelot)
    red_knight.fight(arthur)

    lancelot.death_check()
    arthur.death_check()
    mordred.death_check()
    red_knight.death_check()

    return {
        lancelot.name : lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
