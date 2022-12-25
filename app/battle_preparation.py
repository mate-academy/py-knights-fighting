from __future__ import annotations


class KnightPreparation:

    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 armour: list,
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for ar in self.armour:
            self.protection += ar["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += \
                    self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += \
                    self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += \
                    self.potion["effect"]["hp"]

    def prepare_knight(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
