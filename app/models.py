from __future__ import annotations
from typing import Any, List, Dict, Optional


class Item:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name: str = data.get("name", "Unnamed Item")
        self.power: int = data.get("power", 0)
        self.protection: int = data.get("protection", 0)
        self.part: Optional[str] = data.get("part")
        self.effect: Optional[Dict[str, int]] = data.get("effect")


class Knight:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name: str = data["name"]
        self.base_power: int = data["power"]
        self.hp: int = data["hp"]

        self.armour: List[Item] = [Item(a) for a in data.get("armour", [])]
        self.weapon: Item = Item(data["weapon"])
        self.potion: Optional[Item] = Item(data["potion"]) \
            if data["potion"] else None

        self.total_power: int = 0
        self.total_protection: int = 0

    def prepare_for_battle(self) -> None:
        self.total_power = self.base_power + self.weapon.power

        self.total_protection = sum(a.protection for a in self.armour)

        if self.potion and self.potion.effect:
            effect = self.potion.effect

            self.total_power += effect.get("power", 0)
            self.total_protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def attack(self, target: Knight) -> None:
        damage = max(0, self.total_power - target.total_protection)
        target.hp -= damage

        target.hp = max(0, target.hp)

    def __repr__(self) -> str:
        return (f"Knight(Name={self.name}"
                f", HP={self.hp}"
                f", Power={self.total_power}"
                f", Prot={self.total_protection})")

    @property
    def is_alive(self) -> bool:
        return self.hp > 0
