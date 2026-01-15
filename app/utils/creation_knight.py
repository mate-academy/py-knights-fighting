from app.knight.knight import Knight


def create_knight(data: dict, name: str) -> Knight:
    knight_data = data[name]
    knight = Knight(
        knight_data["name"],
        knight_data["power"],
        knight_data["hp"],
        knight_data["armour"],
        knight_data["weapon"],
        knight_data["potion"],
    )

    # apply armour
    knight.calculate_armour()

    # apply weapon
    knight.calculate_weapon()

    # apply potion if exist
    knight.calculate_potion()

    return knight
