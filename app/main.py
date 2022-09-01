from app.knights.knight_buff.armour import Armour
from app.knights.knight_buff.weapon import Weapon
from app.knights.knight_buff.potion import Potion
from app.knights.all_knights import Knights
from app.knights.finally_battle import Battle
from app.knights.constanta import KNIGHTS


def battle(config):
    all_knights = [Knights(characteristics["name"],
                           name,
                           characteristics["power"],
                           characteristics["hp"]
                           ) for name, characteristics in config.items()]
    for knight in all_knights:
        Potion.apply_potion(config[knight.name_in_dict]["potion"], knight)
        Armour.all_armour(config[knight.name_in_dict]["armour"], knight)
        Weapon.add_weapon(config[knight.name_in_dict]["weapon"], knight)
    Battle.battle(all_knights)
    return {knight.name: knight.hp for knight in all_knights}


print(battle(KNIGHTS))
