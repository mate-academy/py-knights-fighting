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
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> Knight:
        self.protection += sum(
            [armour["protection"] for armour in self.armour]
        )
        return self

    def apply_weapon(self) -> Knight:
        self.power += self.weapon.get("power")
        return self

    def apply_potion(self) -> Knight:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
        return self

    def prepare_battle(self) -> Knight:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self
