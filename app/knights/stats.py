from typing import Dict, List, Optional


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, int]],
        weapon: Dict[str, int],
        potion: Optional[Dict[str, Dict[str, int]]]
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def calculate_stats(self) -> Dict[str, int]:
        protection = sum(part["protection"] for part in self.armour)
        power = self.base_power + self.weapon["power"]
        hp = self.base_hp

        if self.potion:
            effect = self.potion["effect"]
            hp += effect.get("hp", 0)
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)

        return {
            "hp": max(0, hp),
            "power": power,
            "protection": protection,
        }
