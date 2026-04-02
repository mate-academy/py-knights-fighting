from app.battle import Knights
from app.knights import KNIGHTS


def battle(stats: dict) -> dict:
    knights = {
        name: Knights(**attr).apply_equipment()
        for name, attr in stats.items()
    }
    knights["lancelot"].get_hit(knights["mordred"])
    knights["mordred"].get_hit(knights["lancelot"])
    knights["arthur"].get_hit(knights["red_knight"])
    knights["red_knight"].get_hit(knights["arthur"])
    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
