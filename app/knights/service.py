from app.knights.knight import Knight

def make_knights(knights: dict) -> dict:
    new_knights = {}
    for knight_name in knights:
        new_knights[knight_name] = make_knight(knights[knight_name])
    return new_knights

def make_knight(knight: dict) -> Knight:
    name = knight["name"]
    power = knight["power"]
    hp = knight["hp"]
    armour = knight["armour"]
    weapon = knight["weapon"]
    potion = knight["potion"]
    return Knight(name, power, hp, armour, weapon, potion)