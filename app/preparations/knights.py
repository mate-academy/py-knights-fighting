from app.knight.knight import Knight
from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion


def create_knights(knight_config: dict) -> list:
    knights = [
        Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=[
                Armour(
                    part=el["part"], protection=el["protection"])
                for el in knight["armour"]
            ],
            weapon=Weapon(
                name=knight["weapon"]["name"],
                power=knight["weapon"]["power"]
            ),
            potion=Potion(
                name=knight["potion"]["name"],
                effect=knight["potion"]["effect"]
            ) if knight["potion"] is not None else knight["potion"]
        )
        for knight in knight_config.values()
    ]

    return knights
