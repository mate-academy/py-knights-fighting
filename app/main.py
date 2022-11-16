from app.knight_abilities.armour import Armour
from app.knight_abilities.potion import Potion
from app.knight_abilities.weapon import Weapon
from app.knight.warrior import Knight


def knights_items(name: str,  knights_parameters: dict) -> Knight:
    knight = Knight(knights_parameters[name]["name"],
                    knights_parameters[name]["power"],
                    knights_parameters[name]["hp"])
    for armor in  knights_parameters[name]["armour"]:
        armor = Armour(armor["part"], armor["protection"])
        knight.use_armour(armor)
    if  knights_parameters[name]["potion"] is not None:
        potion = Potion(knights_parameters[name]["potion"]["name"],
                        knights_parameters[name]["potion"]["effect"])
        knight.use_potion(potion)
    if knights_parameters[name]["weapon"]:
        weapon = Weapon(knights_parameters[name]["weapon"]["name"],
                        knights_parameters[name]["weapon"]["power"])
        knight.use_weapon(weapon)
    return knight


def battle(config: dict) -> dict:
    lancelot = knights_items("lancelot", config)
    arthur = knights_items("arthur", config)
    mordred = knights_items("mordred", config)
    red_knight = knights_items("red_knight", config)
    result = {lancelot.name: lancelot.battle(mordred),
              mordred.name: mordred.battle(lancelot),
              arthur.name: arthur.battle(red_knight),
              red_knight.name: red_knight.battle(arthur)
              }
    return result
