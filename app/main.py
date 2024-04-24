from app.armour import Armour
from app.info import KNIGHTS
from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = []

    for knight_info in knights_config.values():
        knight = Knight(knight_info)

        for armour in knight.armour:
            knight.apply_armour(Armour(armour))
        knight.apply_weapon(Weapon(knight.weapon))
        if knight.potion:
            knight.apply_potion(Potion(knight.potion))

        knights.append(knight)

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
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
