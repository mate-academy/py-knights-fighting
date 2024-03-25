from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.preparing_knights.knight import Knight


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


def create_knights(knight: dict) -> Knight:
    instance = Knight(
        knight.get("name"),
        knight.get("power"),
        knight.get("hp"),
        create_armour(knight),
        create_weapon(knight),
        create_potion(knight),
    )
    apply_knights(instance)
    return instance


def apply_knights(knight: Knight) -> None:
    if knight.armour:
        knight.protection += sum(
            [armour.protection for armour in knight.armour]
        )

    knight.power += knight.weapon.power

    if knight.potion:
        knight.power += knight.potion.effect.get("power", 0)
        knight.hp += knight.potion.effect.get("hp", 0)
        knight.protection += knight.potion.effect.get(
            "protection", 0
        )
