from app.classes.weapon import Weapon
from app.classes.armour import Armour
from app.classes.potion import Potion
from app.classes.knight import Knight


def creating_knights(knights_config: dict) -> dict[str: Knight]:
    knights = {}

    for name, knight in knights_config.items():
        knights[name] = Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            Weapon(knight["weapon"]["name"], knight["weapon"]["power"]),
            list(Armour(armour["part"], armour["protection"])
                 for armour in knight["armour"]),
        )

        if knight["potion"]:
            knights[name].potion = Potion(
                knight["potion"]["name"],
                knight["potion"]["effect"].get("power", 0),
                knight["potion"]["effect"].get("hp", 0),
                knight["potion"]["effect"].get("protection", 0)
            )

    return knights
