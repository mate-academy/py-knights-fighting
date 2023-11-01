from app.models.models import Knight


def create_knight(knight: dict) -> Knight:
    result = Knight(
        name=knight["name"],
        power=knight["power"],
        hp=knight["hp"]
    )
    if knight["armour"]:
        result.add_armour(knight["armour"])

    result.add_weapon(knight["weapon"])

    if knight["potion"]:
        result.add_potion(knight["potion"])
    return result
