from app.conf.cls_knight import KnightsFighting
from app.conf.dictionary import KNIGHTS


def battle(knights_val: dict) -> dict:
    knights = {
        name: KnightsFighting(**d_conf).apply_equipment()
        for name, d_conf in knights_val.items()
    }

    knights["lancelot"].get_hit(knights["mordred"])
    knights["mordred"].get_hit(knights["lancelot"])
    knights["arthur"].get_hit(knights["red_knight"])
    knights["red_knight"].get_hit(knights["arthur"])

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
