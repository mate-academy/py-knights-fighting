from app.knights.knight_stuff.armour import Armour
from app.knights.knight_stuff.potion import Potion
from app.knights.knight_stuff.weapon import Weapon
from app.knights.knights import Knight


def preprocess_knights_config(knights_config: dict) -> dict:
    result = {}
    for key, value in knights_config.items():
        value = value.copy()
        value["weapon"] = Weapon(**value["weapon"])
        value["armour"] = [Armour(armour.get("part"), armour["protection"])
                           for armour in value.get("armour", [])]
        if value.get("potion"):
            value["potion"] = Potion(**value["potion"])
        result[key] = value
    return result


def create_knights_from_config(knights_config: dict) -> None:
    Knight.knights.clear()
    knights_processed = preprocess_knights_config(knights_config)
    for name, params in knights_processed.items():
        Knight(**params)
