from typing import Dict
from app.knights.knights_stats import Knight


def battle(knightsconfig: Dict) -> Dict:
    knights_dict = {
        name: Knight(**attributes)
        for name, attributes in knightsconfig.items()}
    for knight in knights_dict.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    knights_dict["lancelot"].take_damage(knights_dict["mordred"].power)
    knights_dict["mordred"].take_damage(knights_dict["lancelot"].power)

    knights_dict["arthur"].take_damage(knights_dict["red_knight"].power)
    knights_dict["red_knight"].take_damage(knights_dict["arthur"].power)

    return {knight.name: knight.hp for knight in knights_dict.values()}
