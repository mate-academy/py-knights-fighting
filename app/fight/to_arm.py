from app.knight.knight import Knight
from app.knight.weapon import to_arm_weapon, to_arm_armour, to_arm_potion


def to_arm(knight: Knight) -> Knight:
    knight.protection = to_arm_armour(knight.armour)
    knight.power += to_arm_weapon(knight.weapon)
    knight = to_arm_potion(knight.potion, knight)

    return knight
