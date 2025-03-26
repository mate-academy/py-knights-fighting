def apply_weapon(knight_weapon):
    knight_weapon["power"] += knight_weapon["weapon"]["power"]
    return knight_weapon["power"]
