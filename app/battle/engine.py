from app.utils.knight_utils import apply_armour, apply_weapon, apply_potion, hit

def battle(knights: dict) -> dict:

    knight_names = ["lancelot", "mordred", "arthur", "red"]
    knight_dict = {name: knights[name] for name in knight_names}

    for k in knight_dict.values():
        apply_armour(k)
        apply_weapon(k)
        apply_potion(k)

    def exchange_hits(knight1, knight2):
        hit(knight1, knight2)
        hit(knight2, knight1)
      
    from itertools import combinations
    for k1, k2 in combinations(knight_dict.values(), 2):
        exchange_hits(k1, k2)

    return {name: knight["к.с."] for name, knight in knight_dict.items()}
