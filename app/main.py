from app.inputs.knights_dict import KNIGHTS
from app.knights.ammunition import Armour, Potion, Weapon
from app.knights.knight import Knight
from app.battlefield.battle import Battle


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    knights = Knight.knights_from_dict(knights_config)
    for knight in knights:
        armour = Armour.armours_from_dict(
            knight.tech_name,
            knights_config
        )
        weapon = Weapon.weapon_from_dict(
            knights_config[knight.tech_name]["weapon"]
        )
        potion = Potion.potion_from_dict(
            knights_config[knight.tech_name]["potion"]
        )
        knight.apply_armour(armour)
        knight.apply_weapon(weapon)
        knight.apply_potion(potion)

    # BATTLE:
    for knight in knights:
        if knight.tech_name == "lancelot":
            lancelot = knight
        elif knight.tech_name == "arthur":
            arthur = knight
        elif knight.tech_name == "mordred":
            mordred = knight
        elif knight.tech_name == "red_knight":
            red_knight = knight

    pair_1 = Battle(lancelot, mordred)
    pair_2 = Battle(arthur, red_knight)
    pair_1.battle()
    pair_2.battle()

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
