from app.config.config import KNIGHTS
from app.warrior.knight import Knight
from app.war.preparation import preparation_to_fight
from app.war.battle import start_battle


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    list_of_knights = {}
    for knight in knights_config:
        list_of_knights[knight] = Knight(
            knights_config[knight]["name"],
            knights_config[knight]["power"],
            knights_config[knight]["hp"],
            knights_config[knight]["armour"],
            knights_config[knight]["weapon"],
            knights_config[knight]["potion"]
        )

    # Create lancelot and preparation to fight
    lancelot = list_of_knights["lancelot"]
    preparation_to_fight(lancelot)

    # Create arthur and preparation to fight
    arthur = list_of_knights["arthur"]
    preparation_to_fight(arthur)

    # Create mordred and preparation to fight
    mordred = list_of_knights["mordred"]
    preparation_to_fight(mordred)

    # Create red_knight and preparation to fight
    red_knight = list_of_knights["red_knight"]
    preparation_to_fight(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:
    start_battle(lancelot, mordred)
    start_battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
