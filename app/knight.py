class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict):

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self):
        self.protection = sum(item["protection"] for item in self.armour)
        return self

    def apply_weapon(self):
        self.power += self.weapon["power"]
        return self

    def apply_potion_if_any(self):
        if self.potion is not None:
            for stat in ("power", "hp", "protection"):
                if stat in self.potion["effect"]:
                    setattr(self, stat,
                            getattr(self, stat) + self.potion["effect"][stat])
