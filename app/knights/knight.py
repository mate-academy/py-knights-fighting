class Knight:
    def __init__(
            self,
            name,
            power,
            hp,
            armor,
            weapon,
            potion,
            protection
    ):
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self):
        protection = 0
        for a in self.armor:
            protection += a[protection]
        self.protection = protection

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]


