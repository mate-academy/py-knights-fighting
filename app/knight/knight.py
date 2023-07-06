from __future__ import annotations
from app.ammunition.ammunition import Weapon, Armour, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.apply_ammunition()

    @classmethod
    def from_dict(cls, knight_data: dict) -> Knight:
        armour = [
            Armour(**armour_data) for armour_data in knight_data.pop("armour")
        ]
        weapon = Weapon(**knight_data.pop("weapon"))
        potion = None if (potion_data := knight_data.pop("potion")
                          ) is None else Potion(**potion_data)

        return cls(
            **knight_data,
            armour=armour,
            weapon=weapon,
            potion=potion
        )

    def apply_ammunition(self) -> int:
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
            if "protection" in self.potion.effect:
                self.hp += self.potion.effect["protection"]

        for armour in self.armour:
            self.hp += armour.protection

        self.power += self.weapon.power
        return self.hp | self.power

    def fight(self, other: Knight) -> dict:
        hp_left = self.hp - other.power

        villain_hp_left = other.hp - self.power

        hp_left = max(0, hp_left)
        villain_hp_left = max(0, villain_hp_left)

        # return dict with after fight knight's stats
        return {
            self.name: hp_left,
            other.name: villain_hp_left
        }
