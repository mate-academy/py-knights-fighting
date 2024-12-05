from app.data.item_data import ItemData
from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


class KnightData:
    def __init__(self, config: dict[str, dict]):
        self.name = config.get("name")
        self.hp = config.get("hp")
        self.protection = config.get("protection", 0)
        self.armour = [
            Armour(ItemData(armour_piece))
            for armour_piece in config.get("armour", [])
        ]
        if config.get("weapon"):
            self.weapon = Weapon(ItemData(config.get("weapon")))
        else:
            self.weapon = None

        if config.get("potion"):
            self.potion = Potion(ItemData(config.get("potion")))
        else:
            self.potion = None