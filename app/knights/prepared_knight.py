from app.knights.basic_stats import Knight


def knight_from_dict(data: dict) -> Knight:
    knight = Knight(data["name"], data["power"], data["hp"])

    armour = data.get("armour", [])
    protection = 0
    for part in armour:
        protection += part["protection"]
        knight.protection = protection
    knight.power += data["weapon"]["power"]

    potion = data.get("potion")
    if potion:
        effect = potion.get("effect", {})
        knight.power += effect.get("power", 0)
        knight.hp += effect.get("hp", 0)
        knight.protection += effect.get("protection", 0)
    return knight
