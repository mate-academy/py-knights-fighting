from dataclasses import dataclass


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list
    weapon: dict | None
    potion: dict | None

    def apply_armour(self) -> int:
        self.protection = 0
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]
        return self.protection

    def apply_weapon(self) -> int:
        self.power += self.weapon["power"]
        return self.power

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            for attribute, value in effect.items():
                if hasattr(self, attribute):
                    current_value = getattr(self, attribute)
                    setattr(self, attribute, current_value + value)
