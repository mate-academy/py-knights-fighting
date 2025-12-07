from app.models import Knight
from app.Knights import KNIGHTS


def battle(first: str, second: str) -> dict:
    first = first.lower()
    second = second.lower()
    first_cfg = KNIGHTS.get(first)
    if first_cfg is None:
        raise ValueError("unknown knight")

    second_cfg = KNIGHTS.get(second)
    if second_cfg is None:
        raise ValueError("unknown knight")
    first_knight = Knight(first_cfg)
    second_knight = Knight(second_cfg)
    first_knight.prepare()
    second_knight.prepare()

    damage_for_first = max(0, second_knight.power - first_knight.protection)
    damage_for_second = max(0, first_knight.power - second_knight.protection)

    first_hp_after = first_knight.hp - damage_for_first
    if first_hp_after <= 0:
        first_hp_after = 0
    second_hp_after = second_knight.hp - damage_for_second
    if second_hp_after <= 0:
        second_hp_after = 0
    return {first_cfg["name"]: first_hp_after,
            second_cfg["name"]: second_hp_after}
