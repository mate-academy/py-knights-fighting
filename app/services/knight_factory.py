from app.models.knight import Knight
from app.models.armour import Armour
from app.models.weapon import Weapon
from app.models.potion import Potion


def create_knight(knight_data: dict) -> Knight:
    armour_list = [
        Armour(a["part"], a["protection"])
        for a in knight_data.get("armour", [])
    ]

    weapon_data = knight_data.get("weapon")
    weapon = Weapon(
        weapon_data["name"], weapon_data["power"]) \
        if weapon_data else None

    potion_data = knight_data.get("potion")
    potion = Potion(
        potion_data["name"], potion_data["effect"]) \
        if potion_data else None

    knight = Knight(
        name=knight_data["name"],
        hp=knight_data.get("hp", 0),
        power=knight_data.get("power", 0),
        armour=armour_list,
        weapon=weapon,
        potion=potion
    )

    knight.prepare_for_battle()

    return knight
