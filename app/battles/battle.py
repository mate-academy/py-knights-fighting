def apply_attributes(knight: dict) -> None:
    knight["protection"] = sum(
        armor["protection"] for armor in knight["armour"]
    )
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]
        knight["power"] += potion_effect.get("power", 0)
        knight["protection"] += potion_effect.get("protection", 0)
        knight["hp"] += potion_effect.get("hp", 0)


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        apply_attributes(knight)

    for attacker in knights_config.values():
        for defender in knights_config.values():
            if attacker["name"] != defender["name"]:
                damage = max(0, attacker["power"] - defender["protection"])
                defender["hp"] -= damage
                defender["hp"] = max(0, defender["hp"])

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}


KNIGHTS = {...}
print(battle(KNIGHTS))
