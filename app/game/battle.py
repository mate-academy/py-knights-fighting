from typing import Any


def battle(knights_config: dict[str, dict[str, Any]]) -> dict[str, int]:
    knights = {}

    for key, knight in knights_config.items():
        hp = knight["hp"]
        power = knight["power"] + knight["weapon"]["power"]
        protection = sum(a["protection"] for a in knight["armour"])

        if knight["potion"]:
            effect = knight["potion"]["effect"]
            hp += effect.get("hp", 0)
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)

        knights[key] = {"name": knight["name"],
                        "hp": hp,
                        "power": power,
                        "protection": protection}

    fights = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for knight1_key, knight2_key in fights:
        k1, k2 = knights[knight1_key], knights[knight2_key]

        k1["hp"] -= max(0, k2["power"] - k1["protection"])
        k2["hp"] -= max(0, k1["power"] - k2["protection"])

        k1["hp"] = max(0, k1["hp"])
        k2["hp"] = max(0, k2["hp"])

    return {knight["name"]: knight["hp"] for knight in knights.values()}
