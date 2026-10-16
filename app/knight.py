from typing import Dict, Any, List, Optional


class Knight:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.name: str = config["name"]
        self.power: int = config["power"]
        self.hp: int = config["hp"]
        self.armour: List[Dict[str, Any]] = config.get(
            "armour", []
        )
        self.weapon: Dict[str, Any] = config.get("weapon", {})
        self.potion: Optional[Dict[str, Any]] = config.get(
            "potion"
        )
        self.protection: int = 0
        self.prepare_stats()

    def prepare_stats(self) -> None:
        if self.weapon:
            self.power += self.weapon.get("power", 0)

        for piece in self.armour:
            self.protection += piece.get("protection", 0)

        if self.potion and "effect" in self.potion:
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
