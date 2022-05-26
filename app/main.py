from app.knights_dict import KNIGHTS
from app.knight_class import Knight
from app.battle_func import fight


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    lancelot = Knight(knightsConfig["lancelot"])
    arthur = Knight(knightsConfig["arthur"])
    mordred = Knight(knightsConfig["mordred"])
    red_knight = Knight(knightsConfig["red_knight"])

    # BATTLE:
    fight(lancelot, mordred)
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
