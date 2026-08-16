from typing import Any, Dict, List, Optional


class Knight:
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
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "Knight":
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config.get("armour"),
            weapon=config.get("weapon"),
            potion=config.get("potion"),
        )

    def calculate_protection(self) -> int:
        return sum(piece["protection"] for piece in self.armour)

    def calculate_power(self) -> int:
        power = self.power + (self.weapon["power"] if self.weapon else 0)
        if self.potion is not None:
            power += self.potion["effect"].get("power", 0)
        return power

    def calculate_hp(self) -> int:
        hp = self.hp
        if self.potion is not None:
            hp += self.potion["effect"].get("hp", 0)
        return hp

    def apply_battle_stats(self) -> "Knight":
        protection = self.calculate_protection()
        if self.potion is not None:
            protection += self.potion["effect"].get("protection", 0)

        self.protection = protection
        self.power = self.calculate_power()
        self.hp = self.calculate_hp()
        return self

    def take_damage(self, damage: int) -> int:
        self.hp = max(0, self.hp - damage)
        return self.hp
