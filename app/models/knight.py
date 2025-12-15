from typing import Dict, List, Optional


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: Optional[List[Dict[str, int]]] = None,
                 weapon: Optional[Dict[str, int]] = None,
                 potion: Optional[Dict] = None) -> None:
        self.name: str = name
        self.base_power: int = power
        self.hp: int = hp
        self.armour: List[Dict[str, int]] = armour or []
        self.weapon: Optional[Dict[str, int]] = weapon
        self.potion: Optional[Dict] = potion
        self.power: int = self._apply_weapon_power()
        self.protection: int = self._apply_armour_protection()
        self._apply_potion()

    def _apply_weapon_power(self) -> int:
        weapon_power = self.weapon["power"] if self.weapon else 0
        return self.base_power + weapon_power

    def _apply_armour_protection(self) -> int:
        return sum(piece.get("protection", 0) for piece in self.armour)

    def _apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
