def knight_preparation(knights_config: dict) -> list:
    for knight in knights_config.values():
        knight["protection"] = sum(ammo["protection"]
                                   for ammo in knight["armour"])

        knight["power"] += knight["weapon"]["power"]

        potion = knight.get("potion")
        if potion is not None:
            effects = potion.get("effect", {})
            knight["power"] += effects.get("power", 0)
            knight["protection"] += effects.get("protection", 0)
            knight["hp"] += effects.get("hp", 0)
    return list(knights_config.values())


def fight(knight1: dict, knight2: dict) -> dict:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0

    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"],
    }
