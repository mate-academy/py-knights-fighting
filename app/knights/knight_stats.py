class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @property
    def stats(self):
        total_protection = sum(part["protection"] for part in self.armour)
        total_power = self.power + self.weapon["power"]
        if self.potion:
            for stat, value in self.potion["effect"].items():
                if stat == "hp":
                    self.hp += value
                elif stat == "power":
                    total_power += value
                elif stat == "protection":
                    total_protection += value
        return {
            "hp": self.hp,
            "power": total_power,
            "protection": total_protection,
        }
