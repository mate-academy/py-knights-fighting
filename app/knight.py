from __future__ import annotations


class Knight:

    def __init__(
        self, name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.prepare_knight()

    def prepare_knight(self) -> None:
        self.protection = sum(armour["protection"] for armour in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            for effect_name in ("hp", "power", "protection"):
                potion = getattr(
                    self, effect_name
                )
                setattr(
                    self,
                    effect_name,
                    potion + self.potion["effect"].get(effect_name, 0),
                )

    def __repr__(self) -> None:
        return (
            f"Knight: {self.name}, {self.power}, "
            f"{self.hp}, {self.armour}, {self.weapon}, "
            f"{self.potion}, {self.protection}"
        )

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        elif other.hp <= 0:
            other.hp = 0