from app.skil.model import Knight


def build_knight(knight: dict) -> Knight:
    name = knight.get("name")
    power = knight.get("power", 0)
    hp = knight.get("hp", 0)
    armour = knight.get("armour") or []
    weapon = knight.get("weapon") or {"power": 0}
    potion = knight.get("potion")
    return Knight(name, power, hp, armour, weapon, potion)
