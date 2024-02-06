from typing import Dict

from app.knight.knight import Knight


def battle(
        knights_config: Dict[str, str | int | list[dict] | dict | None]
) -> dict:
    lancelot, arthur, mordred, red_knight = [
        Knight(**knight)
        for knight in knights_config.values()
    ]

    lancelot.receive_damage(mordred.power)
    mordred.receive_damage(lancelot.power)

    arthur.receive_damage(red_knight.power)
    red_knight.receive_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
