from typing import Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Optional[list[dict]] = None,
            weapon: Optional[dict] = None,
            potion: Optional[dict] = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon or {}
        self.potion = potion
        self.protection = 0

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
