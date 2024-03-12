from typing import Dict
from battle.knight import Knight
from battle.weapon import Weapon
from battle.potion import Potion

def prepare_knight(knight_config: Dict) -> Knight:
    name = knight_config["name"]
    power = knight_config["power"]
    hp = knight_config["hp"]
    
    weapon_config = knight_config.get("weapon")
    weapon = Weapon(name=weapon_config["name"], power=weapon_config["power"]) if weapon_config else None
    
    potion_config = knight_config.get("potion")
    if potion_config:
        potion = Potion(
            name=potion_config["name"],
            hp_effect=potion_config.get("effect", {}).get("hp", 0),
            power_effect=potion_config.get("effect", {}).get("power", 0)
        )
    else:
        potion = None
        
    knight = Knight(name=name, power=power, hp=hp, weapon=weapon, potion=potion)
    
    return knight
