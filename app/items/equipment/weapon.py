from __future__ import annotations

from app.items.equipment.eqipment import BaseEquipment
from app.players.player import Player


class Weapon(BaseEquipment):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name=name, power=power)

    @classmethod
    def create_from_dict(cls, weapon: dict | None) -> Weapon | None:
        if not weapon:
            return None
        return cls(weapon["name"], weapon["power"])

    def use(self, player: Player) -> None:
        if not self.is_equipped:
            player.power += self.power
            self.is_equipped = True

    def unuse(self, player: Player) -> None:
        if self.is_equipped:
            player.power -= self.power
            self.is_equipped = False
