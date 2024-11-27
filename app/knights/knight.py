from typing import List, Dict, Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, int]],
            weapon: Dict[str, int],
            potion: Optional[Dict[str, Dict[str, int]]] = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion if potion else {}

    def get_protection(self) -> int:
        return sum(part["protection"] for part in self.armour)

    def get_effective_power(self) -> int:
        weapon_power = self.weapon.get("power", 0)
        potion_power = self.potion.get("effect", {}).get("power", 0)
        return self.power + weapon_power + potion_power

    def get_effective_hp(self) -> int:
        potion_hp = self.potion.get("effect", {}).get("hp", 0)
        return self.hp + potion_hp

    def get_effective_protection(self) -> int:
        potion_protection = self.potion.get("effect", {}).get("protection", 0)
        return self.get_protection() + potion_protection
