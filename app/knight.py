from __future__ import annotations

from app.equipment import Weapon, Armour, Potion


class Knight:
    knights_enlisted: dict[str, Knight] = {}

    def __init__(
            self,
            name: str,
            power: int,
            health: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.protection = protection
        Knight.knights_enlisted[name] = self

    def __str__(self) -> str:
        return (f"{self.name}: power: {self.power}p,"
                f"health: {self.health}p, protection: {self.protection}p.")

    def get_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def put_on_armour_piece(self, armour_piece: Armour) -> None:
        self.protection += armour_piece.protection

    def drink_potion(self, potion: Potion) -> None:
        self.power += potion.power
        self.protection += potion.protection
        self.health += potion.health

    def fight(self, opponent: Knight) -> None:
        self.health -= opponent.power - self.protection
        if self.health < 0:
            self.health = 0
        opponent.health -= self.power - opponent.protection
        if opponent.health < 0:
            opponent.health = 0
