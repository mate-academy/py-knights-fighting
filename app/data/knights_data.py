from typing import Dict
from app.models.knight import Knight
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


def create_knights(knights_config: Dict) -> Dict[str, Knight]:
    knights = {}

    for key, data in knights_config.items():
        knights[key] = Knight(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            weapon=Weapon(**data["weapon"]),
            armour=[Armour(**a) for a in data["armour"]],
            potion=Potion(**data["potion"]) if data["potion"] else None,
        )

    return knights
