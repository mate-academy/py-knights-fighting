from typing import Dict
from app.knights.models import Knight
from app.knights.validators import validate_knight_config


def build_knights_from_config(config: Dict) -> Dict[str, Knight]:

    knights = {}
    for key, data in config.items():
        validate_knight_config(key, data)
        knight = Knight(
            name=data.get("name"),
            base_hp=data.get("hp", 0),
            base_power=data.get("power", 0),
            armour=data.get("armour"),
            weapon=data.get("weapon"),
            potion=data.get("potion"),
        )
        knights[key] = knight

    return knights
