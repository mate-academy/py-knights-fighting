from app.person.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


def prepare_to_battle(knight_data: dict) -> Knight:
    list_of_armour = [
        Armour(item["part"], item["protection"])
        for item
        in knight_data["armour"]
    ]
    weapon = Weapon(
        knight_data["weapon"]["name"],
        knight_data["weapon"]["power"]
    )
    potion = None
    if knight_data["potion"] is not None:
        potion = Potion(
            knight_data["potion"]["name"],
            knight_data["potion"]["effect"]
        )

    knight = Knight(
        knight_data["name"],
        knight_data["power"],
        knight_data["hp"],
        list_of_armour,
        weapon,
        potion
    )

    knight.apply_armour()
    knight.apply_weapon()
    knight.apply_potion()
    return knight
