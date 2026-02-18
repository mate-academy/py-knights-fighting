from typing import List, Dict, Optional, Any


class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Dict[str, Any]]
    weapon: Dict[str, Any]
    potion: Optional[Dict[str, Any]]
    hp: int
    power: int
    protection: int

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[List[Dict[str, Any]]] = None,
        weapon: Optional[Dict[str, Any]] = None,
        potion: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon or {"power": 0}
        self.potion = potion
        self.hp = hp
        self.power = power
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(a.get("protection", 0) for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion.get("effect", {}).items():
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        self.hp = self.hp if self.hp > 0 else 0

    def battle_results(self) -> Dict[str, int]:
        return {self.name: self.hp}
