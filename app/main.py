from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Combatant:
    name: str
    hp: int
    power: int
    protection: int


def _to_combatant(cfg: dict[str, Any]) -> Combatant:
    potion = cfg.get("potion")
    effect = potion.get("effect", {}) if potion else {}

    hp = cfg["hp"] + effect.get("hp", 0)
    power = cfg["power"] + cfg["weapon"]["power"] + effect.get("power", 0)
    protection = (sum(a["protection"]
                  for a in cfg["armour"])
                  + effect.get("protection", 0
                               ))

    return Combatant(
        name=cfg["name"],
        hp=hp,
        power=power,
        protection=protection,
    )


def duel(aa: Combatant, bb: Combatant) -> tuple[int, int]:
    dmg_to_aa = max(0, bb.power - aa.protection)
    dmg_to_bb = max(0, aa.power - bb.protection)

    aa_hp = max(0, aa.hp - dmg_to_aa)
    bb_hp = max(0, bb.hp - dmg_to_bb)
    return aa_hp, bb_hp


def battle(config: dict[str, dict[str, Any]]) -> dict[str, int]:
    lancelot = _to_combatant(config["lancelot"])
    arthur = _to_combatant(config["arthur"])
    mordred = _to_combatant(config["mordred"])
    red_knight = _to_combatant(config["red_knight"])

    l_hp, m_hp = duel(lancelot, mordred)
    a_hp, r_hp = duel(arthur, red_knight)

    return {
        lancelot.name: l_hp,
        arthur.name: a_hp,
        mordred.name: m_hp,
        red_knight.name: r_hp,
    }
