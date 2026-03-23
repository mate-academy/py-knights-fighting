from app.battle_generation.battle import Battle
from typing import Tuple, Dict


def battle(config: dict) -> Tuple[str, dict]:
    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    final: Dict[str, int] = {}
    battle_gen = Battle()
    for key_a, key_b in pairs:
        a_cfg = config[key_a]
        b_cfg = config[key_b]
        result = battle_gen.generate_battle(a_cfg, b_cfg)
        for knight_cfg in (a_cfg, b_cfg):
            name = knight_cfg["name"]
            raw_hp = result.get(name, result.get(name.title(), 0))
            final[name] = max(0, raw_hp)

    return final
