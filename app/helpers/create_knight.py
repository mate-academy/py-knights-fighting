from app.knight.knight import Knight
from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion


def create_knight(cfg: dict) -> Knight:
    return Knight(
        name=cfg["name"],
        power=cfg["power"],
        hp=cfg["hp"],
        armour=[
            Armour(
                part=armour["part"],
                protection=armour["protection"]
            )
            for armour in cfg["armour"]
        ],
        weapon=Weapon(
            name=cfg["weapon"]["name"],
            power=cfg["weapon"]["power"]
        ),
        potion=Potion(
            name=cfg["potion"]["name"],
            effect=cfg["potion"]["effect"]
        )
        if cfg["potion"]
        else None
    )
