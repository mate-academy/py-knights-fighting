from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: List[Dict] = field(default_factory=list)
    weapon: Optional[Dict] = None
    potion: Optional[Dict] = None

    # battle-only attributes
    battle_power: int = field(init=False, default=0)
    battle_hp: int = field(init=False, default=0)
    protection: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        if not self.weapon:
            self.weapon = {"name": "", "power": 0}
        else:
            self.weapon.setdefault("power", 0)

        if not self.potion:
            self.potion = {"name": "", "effect": {}}
        else:
            self.potion.setdefault("effect", {})

        for piece in self.armour:
            piece.setdefault("protection", 0)

    def prepare_for_battle(self) -> None:
        self.protection = sum(
            piece["protection"] for piece in self.armour
        )

        potion_effect = self.potion["effect"]

        self.battle_hp = self.hp + potion_effect.get("hp", 0)

        self.protection += potion_effect.get("protection", 0)

        self.battle_power = (self.power
                             + self.weapon["power"]
                             + potion_effect.get("power", 0))

    def take_damage(self, enemy_power: int) -> None:
        damage = max(0, enemy_power - self.protection)
        self.battle_hp = max(0, self.battle_hp - damage)

    def commit_battle(self) -> None:
        """Apply battle results to base hp."""
        self.hp = self.battle_hp
