

def calculate_armour(armour: list) -> int:
    total = 0
    for item in armour:
        total += item["protection"]
    return total


def calculate_damage(weapon: dict, base_power: int) -> int:
    return base_power + weapon["power"]


def calculate_potion_effect(potion: dict | None) -> dict:
    if potion is None:
        return {"hp": 0, "power": 0, "protection": 0}
    potion_effect = {"hp": 0, "power": 0, "protection": 0}
    for key, value in (potion["effect"].items()):
        potion_effect[key] = value
    return potion_effect
