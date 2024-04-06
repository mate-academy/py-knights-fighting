from __future__ import annotations

from app.items.item import BaseItem
from app.players.player import Player


class Potion(BaseItem):
    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        super().__init__(
            name=name,
            power=power,
            hp=hp,
            protection=protection
        )

    @classmethod
    def create_from_dict(cls, potion: dict | None) -> Potion | None:
        if not potion:
            return None
        name = potion["name"]
        power = potion["effect"].get("power", 0)
        hp = potion["effect"].get("hp", 0)
        protection = potion["effect"].get("protection", 0)
        return cls(name, power, hp, protection)

    def use(self, player: Player) -> None:
        player.power += self.power
        player.hp += self.hp
        player.protection += self.protection
