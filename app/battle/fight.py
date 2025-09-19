from app.knights.knight import Knight
from app.knights.equipment import Armour, Weapon, Potion


def one_vs_one(knight1: Knight, knight2: Knight) -> tuple[int, int]:
    k1 = knight1.final_stats()
    k2 = knight2.final_stats()
    while k1["hp"] > 0 and k2["hp"] > 0:
        k1_damage = max(k2["power"] - k1["protection"], 0)
        k2_damage = max(k1["power"] - k2["protection"], 0)
        k1["hp"] = max(k1["hp"] - k1_damage, 0)
        k2["hp"] = max(k2["hp"] - k2_damage, 0)
    return k1["hp"], k2["hp"]


def battle(knights_config: dict) -> dict[str, int]:
    def build_knight(data: dict) -> Knight:
        armours = [
            Armour(a.get("parte") or a.get("name"),
                   a.get("proteção") or a.get("protection"))
            for a in data.get("armadura", []) + data.get("armours", [])
        ]
        weapon_data = data.get("arma") or data.get("weapon")
        weapon = None
        if weapon_data:
            weapon = Weapon(
                weapon_data.get("nome") or weapon_data.get("name"),
                weapon_data.get("poder") or weapon_data.get("power")
            )
        potion_data = data.get("poção") or data.get("potion")
        potion = None
        if potion_data:
            potion = Potion(
                potion_data.get("nome") or potion_data.get("name"),
                potion_data.get("efeito") or potion_data.get("effect")
            )
        return Knight(
            name=data.get("nome") or data.get("name"),
            base_power=data.get("poder") or data.get("power"),
            base_hp=data.get("hp"),
            armours=armours,
            weapon=weapon,
            potion=potion
        )

    lancelot = build_knight(knights_config["lancelot"])
    mordred = build_knight(knights_config["mordred"])
    arthur = build_knight(knights_config["arthur"])
    red_knight = build_knight(knights_config["red_knight"])

    l_hp, m_hp = one_vs_one(lancelot, mordred)
    a_hp, r_hp = one_vs_one(arthur, red_knight)

    return {
        "Lancelot": l_hp,
        "Arthur": a_hp,
        "Mordred": m_hp,
        "Red Knight": r_hp,
    }
