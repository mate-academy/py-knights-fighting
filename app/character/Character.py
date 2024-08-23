from __future__ import annotations

from app.character import Inventory


class Character:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 inventory: Inventory
                 ) -> None:
        self.name = name
        self.power = power
        self.protection = 0
        self.hp = hp
        self.inventory = inventory
        self.is_alive = True

    def prepare_for_battle(self) -> None:
        for item in self.inventory.items:
            self.power += item.power_bonus
            self.hp += item.hp_bonus
            self.protection += item.protection_bonus

    def hit(self, enemy: Character) -> None:
        enemy.hp -= self.power - enemy.protection
        if enemy.hp <= 0:
            enemy.hp = 0
            enemy.is_alive = False
