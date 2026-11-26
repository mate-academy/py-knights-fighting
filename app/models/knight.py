from typing import Optional, List, Dict, Any


class Knight:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.base_hp: int = data["hp"]
        self.base_power: int = data["power"]
        self.armour: List[Dict[str, Any]] = data.get("armour", [])
        self.weapon: Dict[str, Any] = data["weapon"]
        self.potion: Optional[Dict[str, Any]] = data.get("potion")
        self.hp: int = self.base_hp
        self.power: int = self.base_power
        self.protection: int = 0

        self._equip_armour()
        self._equip_weapon()
        self._drink_potion()

    def _equip_armour(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

    def _equip_weapon(self) -> None:
        self.power += self.weapon["power"]

    def _drink_potion(self) -> None:
        if self.potion is not None:
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
