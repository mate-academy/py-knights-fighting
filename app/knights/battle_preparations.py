from __future__ import annotations


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.protection = sum([a["protection"] for a in knight["armour"]])
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]

    def __repr__(self) -> str:
        return str(self.hp)

    def apply_potion(self, knight: dict) -> Knight:
        if knight["potion"] is not None:
            for effect in knight["potion"]["effect"]:
                self.__setattr__(
                    effect,
                    (self.__getattribute__(effect)
                     + knight["potion"]["effect"][effect])
                )
        return self
