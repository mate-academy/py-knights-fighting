from typing import Dict, Any, Optional


class Knight:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name: str = data["name"]
        self.power: int = data["power"]
        self.hp: int = data["hp"]
        self.armour: Optional[list[Dict[str, int]]] = data.get("armour")
        self.weapon: Dict[str, int] = data["weapon"]
        self.potion: Optional[Dict[str, Any]] = data.get("potion")
        self.protection: int = 0

    def prepare(self) -> None:
        self.protection = 0

        if self.armour:
            for part in self.armour:
                self.protection += part["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            effect: Dict[str, int] = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def fight(self, enemy: "Knight") -> None:
        damage: int = enemy.power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0