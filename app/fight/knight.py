class Knight:
    knights = []

    def __init__(self, name, power, hp, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        Knight.knights.append(self)

    def apply_armor(self):
        for armour in self.armour:
            self.protection += armour['protection']

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if self.potion is not None:
            stats = ("protection", "power", "hp")
            for stat in stats:
                if stat in self.potion["effect"]:
                    setattr(self,
                            stat,
                            getattr(self, stat) + self.potion["effect"][stat])
