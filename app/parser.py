from app.items import Armour, Weapon, Potion
from app.knights import Knight


def parse_knights(knights: dict) -> list:
    result = []
    for name, knight in knights.items():
        potion_list = []
        if knight.get("potion"):
            potion_list = [Potion(
                name=knight["potion"]["name"],
                effect=knight["potion"]["effect"]
                )]
        knight_object = Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=[Armour(
                part=item["part"],
                effect={
                    "protection":item["protection"]
                }
                )
                for item in knight["armour"]
            ],
            weapon= [Weapon(
                name=knight["weapon"]["name"],
                effect={
                    "power": knight["weapon"]["power"]
                }
            )],
            potion=potion_list,
            protection=0
        )
        result.append(knight_object)
    return result
