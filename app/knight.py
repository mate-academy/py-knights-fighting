from typing import List, Dict, Optional


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: Optional[List[Dict]] = None,
                 weapon: Optional[Dict] = None,
                 potion: Optional[Dict] = None
                 ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        self.total_power = self.calculate_total_power()
        self.total_hp = self.calculate_total_hp()
        self.total_protection = self.calculate_total_protection()

    def calculate_total_power(self) -> int:
        weapon_power = self.weapon["power"] if self.weapon else 0
        potion_power = (self.potion["effect"]
                        .get("power", 0)) if self.potion else 0
        return self.base_power + weapon_power + potion_power

    def calculate_total_hp(self) -> int:
        potion_hp = self.potion["effect"].get("hp", 0) if self.potion else 0
        return self.base_hp + potion_hp

    def calculate_total_protection(self) -> int:
        protection = sum(item["protection"] for item in self.armour)
        potion_protection = (self.potion["effect"]
                             .get("protection", 0)) if self.potion else 0
        return protection + potion_protection

    def __str__(self) -> str:
        return (f"{self.name}: Power={self.total_power}, "
                f"HP={self.total_hp}, "
                f"Protection={self.total_protection}")
