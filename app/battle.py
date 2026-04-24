# app/battle.py
from app.knights import Knight


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(**config)
        for key, config in knights_config.items()
    }

    result = {}
    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for first_key, second_key in pairs:
        first = knights[first_key]
        second = knights[second_key]

        first_hp = max(
            0, first.sum_hp() - (second.sum_power() - first.sum_protection())
        )
        second_hp = max(
            0, second.sum_hp() - (first.sum_power() - second.sum_protection())
        )

        result[first.name] = first_hp
        result[second.name] = second_hp

    return result
