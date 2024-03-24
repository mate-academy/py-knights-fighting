from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.preparing_knights.knights import Knights


def create_armour(knight: dict) -> list[Armour]:
    list_armour = knight.get("armour")
    return [
        Armour(armour["part"], armour["protection"])
        for armour in list_armour
    ]


def create_weapon(knight: dict) -> Weapon:
    weapon = knight.get("weapon")
    return Weapon(weapon["name"], weapon["power"])


def create_potion(knight: dict) -> Potion | None:
    if knight.get("potion"):
        potion = knight.get("potion")
        return Potion(potion["name"], potion["effect"])


def create_knights(knights: dict) -> None:
    for name, knight in knights.items():
        Knights(
            knight["name"],
            knight["power"],
            knight["hp"],
            create_armour(knight),
            create_weapon(knight),
            create_potion(knight),
        )
    Knights.apply_knights()
