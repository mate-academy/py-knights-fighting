from typing import List, Dict, Optional, Any


class Knight:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.name: str = config["name"]
        self.base_power: int = config["power"]
        self.hp: int = config["hp"]
        self.armour: List[Dict[str, int]] = config["armour"]
        self.weapon: Dict[str, Any] = config["weapon"]
        self.potion: Optional[Dict[str, Any]] = config["potion"]
        self.power: int = self.base_power
        self.protection: int = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(damage, 0)
        if self.hp < 0:
            self.hp = 0

    def __repr__(self) -> str:
        return f"{self.name}: {self.hp}"
