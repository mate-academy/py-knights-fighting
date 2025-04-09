from app.camelot.knights import Knight
from app.camelot.armour import Armour
from app.camelot.weapon import Weapon
from app.camelot.potion import Potion


def prepare_knight(knight_data: dict) -> Knight:
    knight = Knight(name=knight_data["name"],
                    hp=knight_data["hp"],
                    power=knight_data["power"])

    if "armour" in knight_data and len(knight_data["armour"]) > 0:
        for armour_data in knight_data["armour"]:
            armour = Armour(name=armour_data["part"],
                            protection=armour_data["protection"])
            knight.on_armor(armour=armour)

    if "weapon" in knight_data:
        weapon = Weapon(name=knight_data["weapon"]["name"],
                        power=knight_data["weapon"]["power"])
        knight.take_weapon(weapon=weapon)

    if "potion" in knight_data and knight_data["potion"]:
        potion = Potion(knight_data["potion"]["name"],
                        knight_data["potion"]["effect"])
        knight.drink_potion(potion)

    return knight
