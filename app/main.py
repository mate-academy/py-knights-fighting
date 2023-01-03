from app.knight import Knight
from app.knight_tools.armour import Armour
from app.knight_tools.potion import Potion
from app.knight_tools.weapon import Weapon


def prepare_knights(knights_config: dict) -> list:

    knights_list = []
    for knight, info in knights_config.items():
        knight = Knight(info["name"], info["power"], info["hp"])
        weapon = Weapon(info["weapon"]["name"], info["weapon"]["power"])
        weapon.apply_weapon(knight)
        for armour in info["armour"]:
            armour = Armour(armour["part"], armour["protection"])
            armour.apply_armour(knight)
        if info["potion"] is not None:
            potion = Potion(info["potion"]["name"])
            potion.check_effect(info["potion"]["effect"])
            potion.apply_potion(knight)
        knights_list.append(knight)
    return knights_list


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot, mordred, arthur, red_knight = None, None, None, None
    knights_list = prepare_knights(knights_config)
    for knight in knights_list:
        if knight.name == "Lancelot":
            lancelot = knight
        elif knight.name == "Mordred":
            mordred = knight
        elif knight.name == "Artur":
            arthur = knight
        else:
            red_knight = knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle_round(mordred)
    mordred.battle_round(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.battle_round(red_knight)
    red_knight.battle_round(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
