from app.knights.knights_base import Armour, Knight, Potion, Weapon


def apply_stuff(knights_config: dict) -> dict:
    knights = {}
    for knight_name, knight_value in knights_config.items():
        knight = Knight(
            knight_value["name"],
            knight_value["power"],
            knight_value["hp"]
        )

        if knight_value["armour"]:
            for armour in knight_value["armour"]:
                Armour(armour["part"], armour["protection"])
            knight.add_protection(Armour.armour_list)

        weapon = Weapon(**knight_value["weapon"])
        knight.add_weapon(weapon)

        if knight_value["potion"]:
            potion = Potion(**knight_value["potion"])
            knight.add_potion(potion)

        knights[knight_name] = knight

    return knights
