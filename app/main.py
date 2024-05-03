from app.armour import Armour
from app.knight import Knight
from app.knights_info import KNIGHTS
from app.potion import Potion
from app.weapon import Weapon


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = []

    for knight in knights_config.values():
        knight_ = Knight(knight["name"], knight["power"], knight["hp"])
        for armour in knight["armour"]:
            armour_ = Armour(armour["part"], armour["protection"])
            knight_.get_armour(armour_)

        weapon = Weapon(knight["weapon"]["name"], knight["weapon"]["power"])
        knight_.get_weapon(weapon)
        if knight["potion"] is not None:
            potion = Potion(knight["potion"]["name"],
                            knight["potion"]["effect"])
            knight_.get_potion(potion)
        knights.append(knight_)

    lancelot, arthur, mordred, red_knight = None, None, None, None

    for knight in knights:
        if knight.name == "Lancelot":
            lancelot = knight
        elif knight.name == "Arthur":
            arthur = knight
        elif knight.name == "Mordred":
            mordred = knight
        elif knight.name == "Red Knight":
            red_knight = knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle(mordred)
    mordred.battle(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.battle(red_knight)
    red_knight.battle(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
