class KnightsTemplate:
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

    def add_protection(self) -> "KnightsTemplate":
        for elem in self.armour:
            self.protection += elem["protection"]
        return self

    def add_power(self) -> "KnightsTemplate":
        self.power += self.weapon["power"]
        return self

    def apply_potion(self) -> "KnightsTemplate":
        if "effect" in self.potion and self.potion["effect"] is not None:
            effect = self.potion["effect"]

            if "hp" in effect and effect["hp"] is not None:
                self.hp += effect["hp"]
            if "power" in effect and effect["power"] is not None:
                self.power += effect["power"]
            if "protection" in effect and effect["protection"] is not None:
                self.protection += effect["protection"]

        return self
