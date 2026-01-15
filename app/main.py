from app.data_knights import KNIGHTS
from app.knight import Knight


def battle(knights: dict) -> dict:

    lancelot = Knight(**knights["lancelot"])
    mordred = Knight(**knights["mordred"])
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    arthur = Knight(**knights["arthur"])
    red_knight = Knight(**knights["red_knight"])
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    battle_results = {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }

    return battle_results


battle(KNIGHTS)
