from __future__ import annotations
from app.knigts.knight_on_arena import KnightOnArena


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def prepare_to_battle(self) -> KnightOnArena:
        power = self.power + self.weapon["power"]
        hp = self.hp
        protection = 0
        if self.potion is not None:
            power += self.potion["effect"].get("power", 0)
            hp += self.potion["effect"].get("hp", 0)
            protection += self.potion["effect"].get("protection", 0)
        for part in self.armour:
            protection += part["protection"]
        return KnightOnArena(name=self.name,
                             power=power,
                             hp=hp,
                             protection=protection)
