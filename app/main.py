from typing import Dict

from app.knights.knight import Knight


def battle(knights_data: Dict[str, dict]) -> Dict[str, int]:
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    knights = {name: Knight(**data) for name, data in knights_data.items()}

    for battle_pair in battles:
        knight1, knight2 = knights[battle_pair[0]], knights[battle_pair[1]]
        knight1.apply_effects()
        knight2.apply_effects()

        knight1.hp = max(
            0,
            knight1.hp - max(
                0,
                knight2.power - knight1.protection
            )
        )
        knight2.hp = max(
            0,
            knight2.hp - max(
                0,
                knight1.power - knight2.protection
            )
        )

    return {knight.name: knight.hp for knight in knights.values()}
