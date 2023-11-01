from app.models.models import Knight


def create_knight(knight_data: dict) -> Knight:
    knight = Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"]
    )
    if knight_data["armour"]:
        knight.add_armour(knight_data["armour"])

    knight.add_weapon(knight_data["weapon"])

    if knight_data["potion"]:
        knight.add_potion(knight_data["potion"])
    return knight
