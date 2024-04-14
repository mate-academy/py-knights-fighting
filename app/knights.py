from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def preparing_knight(self) -> Knight:
        self.power += self.weapon["power"]
        for part in self.armour:
            self.protection += part.get("protection", 0)
        if self.potion is not None:
            effect = self.potion.get("effect", {})

            for attribute, value in effect.items():
                setattr(self, attribute, getattr(self, attribute) + value)

        return self


def formation_knight(knight_data: dict) -> Knight:
    knight = Knight(knight_data["name"],
                    knight_data["power"],
                    knight_data["hp"],
                    knight_data["armour"],
                    knight_data["weapon"],
                    knight_data["potion"])
    knight.preparing_knight()

    return knight
