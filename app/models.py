from typing import List, Dict, Optional, Any


class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: List[Dict[str, int]],
            weapon: Dict[str, int],
            potion: Optional[Dict[str, Any]],
    ) -> None:

        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare(self) -> None:
        """Battle preparation: """
        self.protection = sum(a["protection"] for a in (self.armour or []))

        self.power += self.weapon["power"]

        if self.potion:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat, 0) + value)

    def damage(self, opponent_power: int) -> None:
        """Damage from opponent: """
        self.hp -= opponent_power - self.protection
        if self.hp < 0:
            self.hp = 0
