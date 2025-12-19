from app.models.knight import Knight
from app.models.equipment import Armour, Weapon, Potion


def create_knight(config: dict) -> Knight:
    knight = Knight(
        name=config["name"],
        hp=config["hp"],
        power=config["power"],
    )

    armour = [Armour(a["protection"]) for a in config["armour"]]
    weapon = Weapon(config["weapon"]["power"])
    potion = (
        Potion(config["potion"]["effect"])
        if config["potion"] is not None
        else None
    )

    knight.apply_armour(armour)
    knight.apply_weapon(weapon)
    knight.apply_potion(potion)

    return knight
