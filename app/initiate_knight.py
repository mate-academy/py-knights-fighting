from app.knight import Knight


def initiate_the_knight(knight: dict) -> Knight:
    new_knight = Knight(
        name=knight["name"],
        power=knight["power"],
        hp=knight["hp"],
        armour=knight["armour"],
        weapon=knight["weapon"],
        potion=knight["potion"]
    )
    new_knight.apply_armour()
    new_knight.apply_weapon()
    if new_knight.potion is not None:
        new_knight.apply_potion()
    return new_knight
