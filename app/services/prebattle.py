from __future__ import annotations

from typing import Final

from app.domain.models import Knight, Stats

_ALLOWED_EFFECT_KEYS: Final = {"hp", "power", "protection"}


def prepare_stats(knight: Knight) -> Stats:
    protection = sum(a.protection for a in knight.armour)
    power = knight.base_power + (knight.weapon.power if knight.weapon else 0)
    hp = knight.base_hp

    if knight.potion:
        for key, delta in knight.potion.effect.items():
            if key not in _ALLOWED_EFFECT_KEYS:
                continue
            if key == "hp":
                hp += int(delta)
            elif key == "power":
                power += int(delta)
            elif key == "protection":
                protection += int(delta)

    return Stats(
        name=knight.name,
        hp=int(hp),
        power=int(power),
        protection=int(protection),
    )
