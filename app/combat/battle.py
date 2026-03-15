from typing import Dict
from app.knights.models import Knight
from app.combat.rules import apply_damage
from app.utils.helpers import clamp_hp


def battle(a_knight: Knight, b_knight: Knight) -> Dict[str, int]:
    a_stats = a_knight.prepare_stats()
    b_stats = b_knight.prepare_stats()
    a_result_hp, b_result_hp = apply_damage(a_stats, b_stats)
    a_result_hp = clamp_hp(a_result_hp)
    b_result_hp = clamp_hp(b_result_hp)
    return {a_knight.name: a_result_hp, b_knight.name: b_result_hp}
