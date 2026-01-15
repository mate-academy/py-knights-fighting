from typing import List, Optional, Dict


class Knight:
    def __init__(self, config: Dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0
        self.apply_armour(config.get("armour", []))
        self.apply_weapon(config["weapon"])
        self.apply_potion(config.get("potion"))

    def apply_armour(self, armour_list: List[Dict]) -> None:
        for armour in armour_list:
            self.protection += armour["protection"]

    def apply_weapon(self, weapon: Dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: Optional[Dict]) -> None:
        if potion and "effect" in potion:
            effects = potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
