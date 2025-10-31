from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion
from app.models.knight import Knight


def build_knight(data: dict) -> Knight:
    name = data["name"]
    power = data["power"]
    hp = data["hp"]

    armour = []
    for arm in data.get("armour", []):
        armour.append(Armour(arm["part"], arm["protection"]))

    weapon_data = data["weapon"]
    weapon = Weapon(weapon_data["name"], weapon_data["power"])

    potion_data = data.get("potion")
    potion = None
    if potion_data:
        potion = Potion(potion_data["name"], potion_data["effect"])

    return Knight(name, power, hp, armour, weapon, potion)


def duel(k1: Knight, k2: Knight) -> dict:
    k1.take_hit(k2.power)
    k2.take_hit(k1.power)
    return {k1.name: k1.hp, k2.name: k2.hp}
