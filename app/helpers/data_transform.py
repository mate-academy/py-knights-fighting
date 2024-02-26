from app.heroes.knight import Knight
from app.equipment.for_battle import Weapon, ArmourComponent, Potion


def transform_to_knight(knight_data: dict) -> Knight:
    knight = Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        weapon=Weapon(**knight_data["weapon"]),
        armour=[
            ArmourComponent(**armour_component)
            for armour_component in knight_data["armour"]
        ]
    )

    if knight_data["potion"]:
        knight.potion = Potion(**knight_data["potion"])
    return knight
