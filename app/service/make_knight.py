from app.components.knight import Knight
from app.components.weapon import Weapon
from app.components.armour import Armour
from app.components.potion import Potion


def make_knight(knight: dict) -> Knight:
    name = knight["name"]
    power = knight["power"]
    hp = knight["hp"]
    armour = [Armour(armour["part"], armour["protection"])
              for armour in knight["armour"]]
    weapon = Weapon(knight["weapon"]["name"], knight["weapon"]["power"])
    potion = None
    if potion_data := knight.get("potion"):
        potion = Potion(potion_data.get("name"),
                        potion_data.get("effect"))
    return Knight(name, power, hp, armour, weapon, potion)
