from app.service.factory import create_knight
from app.service.combat import duel


def battle(knights_config: dict) -> dict[str, int]:
    knights = {
        name: create_knight(config)
        for name, config in knights_config.items()
    }

    duels = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for first, second in duels:
        duel(knights[first], knights[second])

    return {knight.name: knight.hp for knight in knights.values()}
