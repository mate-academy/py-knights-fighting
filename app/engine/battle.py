from ..knights.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> dict:
    first_stats = first_knight.prepared_stats()
    second_stats = second_knight.prepared_stats()

    damage_to_first = max(0, second_stats["power"] - first_stats["protection"])
    damage_to_second = max(
        0,
        first_stats["power"] - second_stats["protection"]
    )

    first_stats["hp"] = max(0, first_stats["hp"] - damage_to_first)
    second_stats["hp"] = max(0, second_stats["hp"] - damage_to_second)

    battle_result = {
        first_knight.name: first_stats["hp"],
        second_knight.name: second_stats["hp"]
    }
    return battle_result
