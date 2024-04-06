from __future__ import annotations

from app.items.equipment.eqipment import BaseEquipment
from app.players.player import Player


class Armour(BaseEquipment):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name=name, protection=protection)

    @classmethod
    def create_from_dict(cls, armour: dict | None) -> Armour | None:
        if not armour:
            return None
        name = armour["part"]
        protection = armour["protection"]
        return cls(name, protection)

    def use(self, player: Player) -> None:
        if not self.is_equipped:
            player.protection += self.protection
            self.is_equipped = True

    def unuse(self, player: Player) -> None:
        if self.is_equipped:
            player.protection -= self.protection
            self.is_equipped = False
