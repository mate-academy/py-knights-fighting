from __future__ import annotations


class Knight:
    def __init__(
            self: Knight,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None,
    ) -> None:
        # general characteristics
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        # battle characteristics
        self.knight_protection = 0
        self.knight_hp = self.hp
        self.knight_power = self.power

    def protection_calc(self) -> None:
        for armour_pieces in self.armour:
            self.knight_protection += armour_pieces["protection"]

    def power_calc(self) -> None:
        self.knight_power += self.weapon["power"]

    def potion_calc(self) -> None:
        if self.potion is not None:
            for effect_key, effect in self.potion["effect"].items():
                if effect_key == "power":
                    self.knight_power += effect
                if effect_key == "hp":
                    self.knight_hp += effect
                if effect_key == "protection":
                    self.knight_protection += effect
