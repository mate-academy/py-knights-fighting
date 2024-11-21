from app.config.config import KNIGHTS
from app.warrior.knight import Knight
from app.war.preparation import preparation_to_fight
from app.war.battle import start_battle


def battle(knights_config: dict) -> dict:
    # Create dict with knight name and instance
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

    # Preparation to fight for all knights
    for warrior in list_of_knights:
        preparation_to_fight(list_of_knights[warrior])

    # Create knights instance
    lancelot = list_of_knights["lancelot"]
    arthur = list_of_knights["arthur"]
    mordred = list_of_knights["mordred"]
    red_knight = list_of_knights["red_knight"]

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
