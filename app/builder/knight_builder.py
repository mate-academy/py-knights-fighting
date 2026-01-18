from app.models.knight import Knight
from app.models.potion import Potion
from app.models.armour import Armour
from app.models.weapon import Weapon


def build_knight(data: dict) -> Knight:
    armour_list = [
        Armour(item["part"], item["protection"])
        for item in data["armour"]
    ]
    weapon_data = data["weapon"]
    weapon = Weapon(weapon_data["name"], weapon_data["power"])
    potion_data = data["potion"]
    if potion_data is None:
        potion = None
    else:
        potion = Potion(potion_data["name"], potion_data["effect"])
    return Knight(
        data["name"],
        data["power"],
        data["hp"],
        armour_list,
        weapon,
        potion,
    )
