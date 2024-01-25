class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: dict | None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def battle_preparations(self) -> None:
        # apply armour
        self.protection = sum(part["protection"] for part in self.armour)

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion:
            for attribute in (effect := self.potion["effect"]):
                setattr(
                    self,
                    attribute,
                    getattr(self, attribute) + effect[attribute],
                )
