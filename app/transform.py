from app.inventory.armour import Armour
from app.inventory.weapon import Weapon
from app.inventory.potion import Potion
from app.people.knight import Knight


def transform_knights(data: dict) -> list:
    ans = []
    for knight in data:
        armour = [Armour(armor["part"], armor["protection"])
                  for armor in data[knight]["armour"]]
        weapon = Weapon(data[knight]["weapon"]["name"],
                        data[knight]["weapon"]["power"])
        if data[knight]["potion"]:
            potion = Potion(data[knight]["potion"]["name"],
                            data[knight]["potion"]["effect"])
        else:
            potion = None
        ans.append(Knight(data[knight]["name"],
                          data[knight]["power"],
                          data[knight]["hp"],
                          armour, weapon, potion))
    return ans
