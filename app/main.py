from app.knights.knight import Knight
from app.knights.knights_dict import KNIGHTS


def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    lancelot = Knight(knightsConfig["lancelot"])
    lancelot.battle_preparation()
    arthur = Knight(knightsConfig["arthur"])
    arthur.battle_preparation()
    mordred = Knight(knightsConfig["mordred"])
    mordred.battle_preparation()
    red_knight = Knight(knightsConfig["red_knight"])
    red_knight.battle_preparation()

    # BATTLE:
    lancelot.start_battle(mordred)
    arthur.start_battle(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
