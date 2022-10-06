from app.characters.charackers import KNIGHTS
from app.characters.battle_preparation import battle_preparation
from app.characters.fight import fight


def battle(knightsConfig):
    # BATTLE PREPARATIONS:

    knights_dict = battle_preparation(knightsConfig)

    lancelot = knights_dict["lancelot"]
    arthur = knights_dict["arthur"]
    mordred = knights_dict["mordred"]
    red_knight = knights_dict["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:

    fight(lancelot, mordred)

    # # 2 Arthur vs Red Knight:

    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
