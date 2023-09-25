from typing import List, Dict, Union, Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, Union[str, int]]],
            weapon: Dict[str, Union[str, int]],
            potion: Optional[Dict[str, Union[str, int]]]
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.initial_hp = hp
        self.protection = self.apply_armor()  # Инициализация защиты

    def apply_armor(self) -> str:
        protection = sum(armor["protection"] for armor in self.armour)
        return protection

    def apply_weapon(self) -> int:
        return self.base_power + self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.base_power += effect.get("power", 0)
            #self.base_hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def initialize(self) -> None:
        self.protection = self.apply_armor()
        self.power = self.apply_weapon()
        self.hp = self.base_hp
        self.apply_potion()
