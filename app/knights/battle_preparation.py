from __future__ import annotations


class Knight:

    def __init__(self, name: str,
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
        self.protection = sum([protect.get("protection")
                               for protect in self.armour])
        self.apply_weapon()
        self.apply_potion()

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion.get("effect"):
                self.power += (self.potion.get("effect")
                               .get("power"))
            if "protection" in self.potion.get("effect"):
                self.protection += (self.potion.get("effect")
                                    .get("protection"))
            if "hp" in self.potion.get("effect"):
                self.hp = (self.hp + self.potion.get("effect")
                           .get("hp"))
