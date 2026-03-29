from typing import Dict, Union, List
from app.knights.knight import Knight


def battle(
    knights_config: Dict[
        str, Dict[str, Union[str, int, List[Dict[str, int]]]]
    ]
) -> Dict[str, int]:
    knights = {}
    for key, value in knights_config.items():
        knight = Knight(value["name"], value["power"], value["hp"],
                        value["armour"], value["weapon"], value["potion"])
        knight.update_stats()
        knights[key] = knight

    # battle logic
    lancelot_damage = max(
        0, knights["mordred"].power - knights["lancelot"].protection
    )
    mordred_damage = max(
        0, knights["lancelot"].power - knights["mordred"].protection
    )

    knights["lancelot"].hp -= lancelot_damage
    knights["mordred"].hp -= mordred_damage

    arthur_damage = max(
        0, knights["red_knight"].power - knights["arthur"].protection
    )
    red_knight_damage = max(
        0, knights["arthur"].power - knights["red_knight"].protection
    )

    knights["arthur"].hp -= arthur_damage
    knights["red_knight"].hp -= red_knight_damage

    return {
        knight.name: max(0, knight.hp) for knight in knights.values()
    }
