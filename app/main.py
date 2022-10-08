from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon
from app.knight import Knight
from app.knights_list import KNIGHTS


def knights_items(name: str, parametrs: dict) -> Knight:
    knight = Knight(parametrs[name]["name"],
                    parametrs[name]["power"],
                    parametrs[name]["hp"])
    for armour in parametrs[name]["armour"]:
        arm = Armour(armour["part"], armour["protection"])
        knight.use_armour(arm)
    if parametrs[name]["potion"] is not None:
        potion = Potion(parametrs[name]["potion"]["name"],
                        parametrs[name]["potion"]["effect"])
        knight.use_potion(potion)
    if parametrs[name]["weapon"]:
        wpn = Weapon(parametrs[name]["weapon"]["name"],
                     parametrs[name]["weapon"]["power"])
        knight.use_weapon(wpn)
    return knight


def battle(config: int) -> dict:
    lancelot = knights_items("lancelot", config)
    arthur = knights_items("arthur", config)
    mordred = knights_items("mordred", config)
    red_knight = knights_items("red_knight", config)
    result = {}
    result.update({lancelot.name: lancelot.battle(mordred)})
    result.update({mordred.name: mordred.battle(lancelot)})
    result.update({arthur.name: arthur.battle(red_knight)})
    result.update({red_knight.name: red_knight.battle(arthur)})
    return result


print(battle(KNIGHTS))
