from app.knights.knight import Knight
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion


def create_knight(knight_info: dict) -> Knight:
    # Creating Knight, Weapon, Potion, and Armour list
    # and applying all these items to Knight
    knight = Knight(
        knight_info["name"],
        knight_info["power"],
        knight_info["hp"]
    )
    weapon = Weapon(
        knight_info["weapon"]["name"],
        knight_info["weapon"]["power"]
    )
    armour_list = []

    for armour in knight_info["armour"]:
        armour_list.append(Armour(
            armour["part"],
            armour["protection"]
        ))

    if knight_info["potion"]:
        potion = Potion(
            knight_info["potion"]["name"],
            knight_info["potion"]["effect"]
        )
        knight.apply_potion(potion)

    knight.apply_armour(armour_list)
    knight.apply_weapon(weapon)

    return knight
