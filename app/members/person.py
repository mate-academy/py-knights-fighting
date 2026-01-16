from app.members.fighter import Fighter
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion


def create_knight(knight_info: dict) -> Fighter:
    fighter = Fighter(
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
        fighter.apply_potion(potion)

    fighter.apply_armour(armour_list)
    fighter.apply_weapon(weapon)

    return fighter
