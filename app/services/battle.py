# app/services/battle.py

from app.models.knight import Knight


def fight(first: Knight, second: Knight) -> dict[str, int]:
    first_hp = (
        first.battle_hp
        - (second.battle_power - first.protection)
    )

    second_hp = (
        second.battle_hp
        - (first.battle_power - second.protection)
    )

    return {
        first.name: max(0, first_hp),
        second.name: max(0, second_hp),
    }
