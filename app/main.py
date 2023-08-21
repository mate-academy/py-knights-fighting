from app.knight.equipment.armour import Armour
from app.knight.equipment.weapon import Weapon
from app.knight.equipment.potion import Potion
from app.knight.knights import Knights
from app.knight.fight import Battle
from app.knight.data import KNIGHTS


def battle(config: dict) -> dict:
    all_knights = [
        Knights(
            characteristics["name"],
            name,
            characteristics["power"],
            characteristics["hp"]
        )
        for name, characteristics in config.items()
    ]
    for knight in all_knights:
        Potion.apply_potion(config[knight.name_in_dict]["potion"], knight)
        Armour.all_armour(config[knight.name_in_dict]["armour"], knight)
        Weapon.add_weapon(config[knight.name_in_dict]["weapon"], knight)
    Battle.battle(all_knights)
    return {knight.name: knight.hp for knight in all_knights}


print(battle(KNIGHTS))
