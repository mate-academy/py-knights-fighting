class Knight:

    def __init__(
            self, name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    def apply_modifiers(self) -> Knight:
        if self.weapon:
            self.power += self.weapon["power"]
        if self.armour:
            total_protection = sum(item["protection"] for item in self.armour)
            self.protection += total_protection
        if self.potion:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "protection" in effect:
                self.protection += effect["protection"]
        return self
