from app.armor.ammunition import Armour, Weapon, Potion
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = Knight.all_knights(knights_config)
    for i in range(len(knights)):
        knight = knights[i]
        armour = Armour.armours_from_dict(
            knights_config,
            knight.tech_name
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
