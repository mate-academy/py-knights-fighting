from typing import Dict
from app.knight import Knight


def battle(
        knights_config: Dict[str, dict]
) -> Dict[str, int]:
    knights = {name: Knight(**info) for name, info in knights_config.items()}

    for knight in knights.values():
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    # Battle
    knights["lancelot"].hp -= (
        knights["mordred"].power - knights["lancelot"].protection
    )
    knights["mordred"].hp -= (
        knights["lancelot"].power - knights["mordred"].protection
    )

    knights["arthur"].hp -= (
        knights["red_knight"].power - knights["arthur"].protection
    )
    knights["red_knight"].hp -= (
        knights["arthur"].power - knights["red_knight"].protection
    )

    # Check if someone fell in battle
    for knight in knights.values():
        if knight.hp <= 0:
            knight.hp = 0

    return {knight.name: knight.hp for knight in knights.values()}
