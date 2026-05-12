from app.knights.armour import Armour
from app.knights.knight import Knight
from app.knights.potion import Potion
from app.knights.weapon import Weapon


def create_knight(data: dict) -> Knight:
    weapon = Weapon(
        name=data["weapon"]["name"],
        power=data["weapon"]["power"],
    )

    armour = [
        Armour(
            part=piece["part"],
            protection=piece["protection"],
        )
        for piece in data["armour"]
    ]

    potion = None

    if data["potion"] is not None:
        potion = Potion(
            name=data["potion"]["name"],
            effect=data["potion"]["effect"],
        )

    return Knight(
        name=data["name"],
        hp=data["hp"],
        power=data["power"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )
