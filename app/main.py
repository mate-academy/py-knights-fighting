from app.armour import Armour
from app.info import KNIGHTS
from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {}

    for knight_info in knights_config.values():
        knight = Knight(knight_info)

        for armour in knight.armour:
            knight.apply_armour(Armour(armour))
        knight.apply_weapon(Weapon(knight.weapon))
        if knight.potion:
            knight.apply_potion(Potion(knight.potion))

        knights[knight.name] = knight

    lancelot = knights.get("Lancelot")
    arthur = knights.get("Arthur")
    mordred = knights.get("Mordred")
    red_knight = knights.get("Red Knight")
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle(mordred)

    # 2 Arthur vs Red Knight:
    arthur.battle(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
