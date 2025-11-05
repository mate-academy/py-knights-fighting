from app.models.knight import Knight


def calc_after(attacker: dict[str, int], defender: dict[str, int]) -> int:
    damage = max(0, attacker["power"] - defender["protection"])
    hp_after = max(0, defender["hp"] - damage)
    return hp_after


def fight(left_knight: Knight, right_knight: Knight) -> dict[str, int]:
    left_stats = left_knight.get_stats()
    right_stats = right_knight.get_stats()
    left_name = left_stats["name"]
    right_name = right_stats["name"]
    left_hp_after = calc_after(right_stats, left_stats)
    right_hp_after = calc_after(left_stats, right_stats)

    return {left_name: left_hp_after, right_name: right_hp_after}
