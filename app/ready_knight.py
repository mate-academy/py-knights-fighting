from app.knight import Knight
from app import equipment


def create_knight(knight_data: dict) -> Knight:
    protection = equipment.calculate_armour(knight_data["armour"])
    name = knight_data["name"]
    hp = knight_data["hp"]
    power = equipment.calculate_damage(
        knight_data["weapon"],
        knight_data["power"]
    )
    potion = equipment.calculate_potion_effect(knight_data["potion"])
    hp += potion["hp"]
    power += potion["power"]
    protection += potion["protection"]
    return Knight(name, hp, power, protection)
