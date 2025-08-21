from typing import Optional, List, Dict

class Knight:
    def __init__(self, config: Dict[str, any]) -> None:
        self.name: str = config.get("name", "Unknown Knight")
        self.base_hp: int = config.get("hp", 0)
        self.base_power: int = config.get("power", 0)
        self.armour: List[Dict[str, int]] = config.get("armour", [])
        self.weapon: Dict[str, int] = config.get("weapon", {"power": 0})
        self.potion: Optional[Dict[str, Dict[str, int]]] = config.get("potion")

        self.hp: int = self.calculate_hp()
        self.power: int = self.calculate_power()
        self.protection: int = self.calculate_protection()

    def calculate_hp(self) -> int:
        effect: Dict[str, int] = self.potion.get("effect", {}) if self.potion else {}
        return self.base_hp + effect.get("hp", 0)

    def calculate_power(self) -> int:
        effect: Dict[str, int] = self.potion.get("effect", {}) if self.potion else {}
        return self.base_power + self.weapon.get("power", 0) + effect.get("power", 0)

    def calculate_protection(self) -> int:
        base: int = sum(part.get("protection", 0) for part in self.armour)
        effect: Dict[str, int] = self.potion.get("effect", {}) if self.potion else {}
        return base + effect.get("protection", 0)
