from typing import Dict, Any
from app.data.knights import KNIGHTS
from app.models.knight import Knight
from app.fight.battle import Battle


def battle(knights: dict | None = None) -> Dict:
    data = knights if knights is not None else KNIGHTS

    def prepare_knight(raw: Dict[str, Any]) -> Dict[str, Any]:
        name = raw["name"]
        base_hp = raw.get("hp", 0)
        base_power = raw.get("power", 0)
        weapon = raw.get("weapon") or {}
        weapon_power = weapon.get("power", 0)
        armour = raw.get("armour") or []
        protection = sum(part.get("protection", 0) for part in armour)
        potion = raw.get("potion")

        if potion and isinstance(potion.get("effect"), dict):
            eff = potion["effect"]
            hp = base_hp + eff.get("hp", 0)
            power = base_power + weapon_power + eff.get("power", 0)
            protection = protection + eff.get("protection", 0)
        else:
            hp = base_hp
            power = base_power + weapon_power

        return {
            "name": name,
            "hp": int(hp),
            "power": int(power),
            "protection": int(protection),
        }

    prepared = {key: prepare_knight(data[key])
                for key in ("lancelot", "mordred", "arthur", "red_knight")}

    pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    results = {}
    for knight1, knight2 in pairs:
        battle_result = Battle(Knight(prepared[knight1]),
                               Knight(prepared[knight2])).fight()
        results.update(battle_result)
    return results
