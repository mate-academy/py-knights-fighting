def apply_attributes(knight):
    knight["protection"] = sum(armor["protection"] for armor in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]
        knight["power"] += potion_effect.get("power", 0)
        knight["protection"] += potion_effect.get("protection", 0)
        knight["hp"] += potion_effect.get("hp", 0)

def battle(knightsConfig):
    for knight_name, knight in knightsConfig.items():
        apply_attributes(knight)

    for attacker_name, attacker in knightsConfig.items():
        for defender_name, defender in knightsConfig.items():
            if attacker_name != defender_name:
                damage = max(0, attacker["power"] - defender["protection"])
                defender["hp"] -= damage
                defender["hp"] = max(0, defender["hp"])

    return {knight["name"]: knight["hp"] for knight in knightsConfig.values()}

KNIGHTS = {...}
print(battle(KNIGHTS))
