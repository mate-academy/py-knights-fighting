from app.inventory.armour import Armour
from app.inventory.weapon import Weapon
from app.inventory.potion import Potion
from app.people.knight import Knight


def transform_knights(data: dict) -> dict:
    ans = {}
    for name, knight in data.items():
        armour = [Armour(armor["part"], armor["protection"])
                  for armor in knight["armour"]]
        weapon = Weapon(knight["weapon"]["name"],
                        knight["weapon"]["power"])
        if knight["potion"]:
            potion = Potion(knight["potion"]["name"],
                            knight["potion"]["effect"])
        else:
            potion = None
        ans[name] = Knight(knight["name"], knight["power"],
                           knight["hp"], armour, weapon, potion)
    return ans
