from app.knight_configure import KNIGHTS
from app.knight_class import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    ## CREATE KNIGHTS
    all_knights = {}
    for knight, param in knights_config.items():
        all_knights[knight] = Knight(
            param["name"],
            param["power"],
            param["hp"]
        )

    ## АDD KNIGHTS EQUIPMENTS
    for knight_name in all_knights:
        config = knights_config[knight_name]
        knights = all_knights[knight_name]

        if "armour" in config:
            armour_list = config["armour"]
            knights.add_armours(armour_list)

        if "potion" in config and isinstance(config["potion"], dict):
            knights.add_potion(config["potion"])

        if "weapon" in config:
            knights.add_weapon(config["weapon"])

    # -------------------------------------------------------------------------------
    # BATTLE:
    ## tournament participants
    lancelot = all_knights["lancelot"]
    mordred = all_knights["mordred"]
    arthur = all_knights["arthur"]
    red_knight = all_knights["red_knight"]

    # 1 Lancelot vs Mordred:
    lancelot.attack(mordred)
    mordred.attack(lancelot)
    # 2 Arthur vs Red Knight:
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
