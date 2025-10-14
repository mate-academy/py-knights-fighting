from typing import Dict
from app.battle.duel import duel
from app.data.knights_data import knights_data

def battle(knights_config: Dict) -> Dict[str, int]:
    from app.knights.knight import Knight

    knights = {}
    for key, data in knights_config.items():
        knights[key] = Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data.get("armour", []),
            weapon=data.get("weapon", {}),
            potion=data.get("potion"),
        )

    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    results = {}
    for k in ["lancelot", "arthur", "mordred", "red_knight"]:
        knight = knights[k]
        hp_val = knight.hp
        if hp_val < 0:
            hp_val = 0
        results[knight.name] = hp_val

    return results

if __name__ == "__main__":
    results = battle(knights_data)
    print("Battle results:", results)
