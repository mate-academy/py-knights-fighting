from typing import Dict, List, Optional


class Knight:
    def __init__(self, config: Dict) -> None:
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.power: int = config["power"]
        self.protection: int = 0

        self._equip_armour(config.get("armour", []))
        self._equip_weapon(config.get("weapon", {}))
        self._drink_potion(config.get("potion"))

    def _equip_armour(self, armour_list: List[Dict]) -> None:
        for item in armour_list:
            self.protection += item.get("protection", 0)

    def _equip_weapon(self, weapon: Dict) -> None:
        self.power += weapon.get("power", 0)

    def _drink_potion(self, potion: Optional[Dict]) -> None:
        if potion:
            effect = potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
