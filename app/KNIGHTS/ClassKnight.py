from __future__ import annotations


class Knight:

    """
The Knight class is designed for a simpler way of computing
battle result and store information
    """

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict | None
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.potion = potion
        # Preparation to the fight

        for item in armour:
            self.protection += item["protection"]

        # Arming

        self.power += weapon["power"]

    def using_potion(self) -> None:

        if self.potion:

            for effect, value in self.potion["effect"].items():
                setattr(self, effect, getattr(self, effect, 0) + value)

    def fight(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        # checking if someone fell in the battle

        self.hp = 0 if self.hp < 0 else self.hp

        enemy.hp = 0 if enemy.hp < 0 else enemy.hp
