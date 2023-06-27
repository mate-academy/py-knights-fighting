from app.battles.battle_preparations import get_prepared_knights
from app.battles.fight import fight


def battle(knights_data: dict[str, dict]) -> dict:
    knights = get_prepared_knights(knights_data)
    result = {}

    fight(knights.get("lancelot"), knights.get("mordred"))
    fight(knights.get("arthur"), knights.get("red_knight"))

    for knight in knights.values():
        if knight.hp < 0:
            knight.hp = 0

        result[knight.name] = knight.hp

    return result
