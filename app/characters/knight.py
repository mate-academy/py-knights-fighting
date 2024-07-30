from __future__ import annotations


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list | None,
        weapon: dict,
        potion: dict = None,
        protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def get_armour(self) -> None:
        self.protection = sum(elem["protection"] for elem in self.armour)

    def get_weapon(self) -> None:
        self.power += self.weapon["power"]

    def get_potion(self) -> int | None:
        if self.potion is None:
            return 0
        effect = self.potion.get("effect", {})
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def get_ready(self) -> Knight:
        self.get_armour()
        self.get_weapon()
        self.get_potion()
        return self
