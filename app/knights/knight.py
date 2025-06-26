from __future__ import annotations


class Knight:

    protection = 0

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

    def apply_armour(self) -> Knight:
        self.protection += sum([armour["protection"]
                                for armour in self.armour])
        return self

    def apply_weapon(self) -> Knight:
        self.power += self.weapon.get("power")
        return self

    def apply_potion(self) -> Knight:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
        return self

    def prepare_battle(self) -> Knight:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self
