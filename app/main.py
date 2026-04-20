from typing import Dict
from app.data.knights import KNIGHTS
from app.models.knight import Knight
from app.fight.battle import Battle


def battle(knights: dict | None = None) -> Dict:
    data = knights if knights is not None else KNIGHTS

    def prepare_knight(raw: dict) -> dict:
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

    res_a = Battle(Knight(prepared["lancelot"]),
                   Knight(prepared["mordred"])).fight()
    res_b = Battle(Knight(prepared["arthur"]),
                   Knight(prepared["red_knight"])).fight()

    result = {
        prepared["lancelot"]["name"]: max(0,
                                          res_a[prepared["lancelot"]["name"]]),
        prepared["mordred"]["name"]: max(0,
                                         res_a[prepared["mordred"]["name"]]),
        prepared["arthur"]["name"]: max(0,
                                        res_b[prepared["arthur"]["name"]]),
        prepared["red_knight"]["name"]: max(
            0,
            res_b[prepared["red_knight"]["name"]]
        ), }

    return result


if __name__ == "__main__":
    print(battle())
