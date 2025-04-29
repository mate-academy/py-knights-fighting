from knights.armour import Armour
from knights.weapon import Weapon
from knights.potion import Potion


class Knight:
    knight_protection = 0

    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.armours = self.get_armour(knight_config["armour"])
        self.weapon = self.get_weapon(knight_config["weapon"])
        self.potion = self.get_potion(knight_config["potion"])

    @staticmethod
    def get_armour(armour_config: list) -> list:
        if len(armour_config) == 0:
            print("Knight haven't armour!")
            return []
        return [Armour(armour) for armour in armour_config]

    @staticmethod
    def get_weapon(weapon_config: dict) -> Weapon:
        return Weapon(weapon_config)

    @staticmethod
    def get_potion(potion_config: dict | None) -> Potion | None:
        if potion_config is None:
            return None
        return Potion(potion_config)
