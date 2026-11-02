from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = 0

        for piece in armour:
            self.protection += piece["protection"]

        if potion is not None:
            self.power += potion["effect"].get("power", 0)
            self.hp += potion["effect"].get("hp", 0)
            self.protection += potion["effect"].get("protection", 0)

    def fight(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection

    def check_hp(self) -> None:
        self.hp = self.hp if self.hp > 0 else 0
