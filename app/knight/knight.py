from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
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

    def apply_armour(self) -> None:
        self.protection = sum([a["protection"] for a in self.armour])

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]

    def prepare_knight(self) -> Knight:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self
