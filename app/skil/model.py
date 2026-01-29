from typing import Optional


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Optional[list],
            weapon: dict,
            potion: Optional[dict]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.prepared = False

    def prepare(self) -> None:
        if self.prepared:
            return

        # apply armour
        self.protection = 0
        for part in self.armour:
            self.protection += part["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            effect = self.potion.get("effect", {})
            for key in ("power", "protection", "hp"):
                if key in effect:
                    setattr(self, key, getattr(self, key) + effect[key])

        self.prepared = True
