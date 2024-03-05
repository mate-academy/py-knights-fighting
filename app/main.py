from app.armor.ammunition import Armour, Weapon, Potion
from app.knights.knight import Knight


def battle(knightsConfig: dict) -> dict:
    knights = Knight.all_knights(knightsConfig)
    for i in range(4):
        knight = knights[i]
        armour = Armour.armours_from_dict(
            knightsConfig,
            knight.tech_name
        )

        weapon = Weapon.weapon_from_dict(
            knightsConfig[knight.tech_name]["weapon"]
        )

        potion = Potion.potion_from_dict(
            knightsConfig[knight.tech_name]["potion"]
        )

        knight.apply_armour(armour)
        knight.apply_weapon(weapon)
        knight.apply_potion(potion)
