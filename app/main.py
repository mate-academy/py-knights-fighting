from app.knights_configuration import knights_configuration
from app.knights_list import knights


def battle(knights):

    # BATTLE PREPARATIONS:

    configured_knights = knights_configuration(knights)

    # 1 Lancelot vs Mordred:

    lancelot = configured_knights["lancelot"]
    mordred = configured_knights["mordred"]

    lancelot.versus(mordred)

    # 2 Arthur vs Red Knight:

    arthur = configured_knights["arthur"]
    red_knight = configured_knights["red_knight"]

    arthur.versus(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(knights))
