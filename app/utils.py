from typing import List, Dict, Iterable
from app.entities import Knight


def sum_protection(armour: List[Dict]) -> int:
    return sum(part.get("protection", 0) for part in (armour or []))


def apply_weapon(base_power: int, weapon: Dict | None) -> int:
    return base_power + (weapon.get("power", 0) if weapon else 0)


def apply_damage(defender: Knight, attacker_power: int) -> None:
    defender.take_damage(attacker_power)


KEYS = ("hp", "power", "protection")


def apply_potion(stats: Dict[str, int], potion: Dict | None) -> Dict[str, int]:
    """Застосувати ефект зілля до stats (тільки для ключів у KEYS)."""
    result = stats.copy()
    if not potion:
        return result
    effect = potion.get("effect", {})
    for key in KEYS:
        if key in effect:
            result[key] = result.get(key, 0) + effect[key]
    return result


def clamp_hp(hp: int) -> int:
    return max(hp, 0)


def create_knights(
        knights_config: Dict[str, dict], keys: Iterable[str]
) -> Dict[str, dict]:
    result: dict = {}
    for key in keys:
        cfg = knights_config.get(key)
        if cfg is None:
            raise KeyError(f"Missing knight config for key: {key}")

        knight = Knight(cfg)
        knight.prepare()
        result[key] = knight

    return result
