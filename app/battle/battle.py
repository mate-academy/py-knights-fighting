from app.data.knights_data import create_all_knights
from app.models.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:

    damage_to_first_knight = max(
        0,
        second_knight.power - first_knight.protection
    )
    damage_to_second_knight = max(
        0,
        first_knight.power - second_knight.protection
    )
    first_knight.take_damage(damage_to_first_knight)
    second_knight.take_damage(damage_to_second_knight)


def tournament(knights_data: dict) -> dict:
    knights = create_all_knights(knights_data)

    for knight in knights.values():
        knight.prepare_for_battle()

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
