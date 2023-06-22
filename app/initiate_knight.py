from app.knight import Knight


def initiate_the_knight(knight: dict) -> Knight:
    knight_obj = Knight(
        name=knight["name"],
        power=knight["power"],
        hp=knight["hp"],
        armour=knight["armour"],
        weapon=knight["weapon"],
        potion=knight["potion"]
    )
    knight_obj.apply_armour()
    knight_obj.apply_weapon()
    if knight_obj.potion is not None:
        knight_obj.apply_potion()
    return knight_obj
