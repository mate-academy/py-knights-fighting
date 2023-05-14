from typing import Dict, List, Union

class Knight:
    def __init__(self, config: Dict[str, Union[str, int, List[Dict[str, int]], Dict[str, Union[str, Dict[str, int]]]]]) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.protection = 0

    def apply_armour(self):
        for a in self.armour:
            self.protection += a["protection"]

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def attack(self, opponent) -> None:
        opponent.hp -= max(self.power - opponent.protection, 0)
        opponent.hp = max(opponent.hp, 0)
