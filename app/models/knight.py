from typing import Dict, List, Any
from app.models.armour import Armour
from app.models.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, Any]],
        weapon: Dict[str, Any],
        potion: Dict[str, Any] | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        for item in armour:
            Armour(**item).apply(self)
        Weapon(**weapon).apply(self)

        if potion:
            for stat, value in potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)
