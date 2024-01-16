from typing import Dict, Any

from app.knights_config import knights_config


def apply_effects(knight: Dict[str, Any]) -> None:
    knight["protection"] = sum(
        armor["protection"] for armor in knight["armour"]
    )
    knight["power"] += knight["weapon"].get("power", 0)
    if knight["potion"]:
        effect = knight["potion"]["effect"]
        for attribute in ["power", "protection", "hp"]:
            knight[attribute] += effect.get(attribute, 0)


def conduct_battle(knight1: Dict[str, Any], knight2: Dict[str, Any]) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    for knight in knights_config.values():
        apply_effects(knight)

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for knight1_name, knight2_name in battles:
        knight1 = knights_config[knight1_name]
        knight2 = knights_config[knight2_name]
        conduct_battle(knight1, knight2)

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


def main() -> None:
    results: Dict[str, int] = battle(knights_config)
    print(results)


if __name__ == "__main__":
    main()
