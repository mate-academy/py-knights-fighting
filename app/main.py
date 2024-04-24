from app.armour import Armour
from app.knight import Knight
from app.knights_info import KNIGHTS
from app.potion import Potion
from app.weapon import Weapon


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {}

    for knight_data in knights_config.values():
        knight = Knight(knight_data["name"],
                        knight_data["power"],
                        knight_data["hp"])
        for armour_data in knight_data["armour"]:
            armour = Armour(armour_data["part"], armour_data["protection"])
            knight.get_armour(armour)

        weapon_data = knight_data["weapon"]
        weapon = Weapon(weapon_data["name"], weapon_data["power"])
        knight.get_weapon(weapon)

        if knight_data["potion"] is not None:
            potion_data = knight_data["potion"]
            potion = Potion(potion_data["name"], potion_data["effect"])
            knight.get_potion(potion)

        knights[knight_data["name"]] = knight

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
        knight.name: knight.hp
        for knight in [lancelot, arthur, mordred, red_knight]
    }


print(battle(KNIGHTS))
