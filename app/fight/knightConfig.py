class Knights:

    def __init__(self, knights_char):
        self.name = knights_char["name"]
        self.power = knights_char["power"]
        self.hp = knights_char["hp"]
        self.armour = knights_char["armour"]
        self.weapon = knights_char["weapon"]
        self.potion = knights_char["potion"]
        self.protection = 0
        self.preparation_for_battle()

    def preparation_for_battle(self):
        self.power += self.weapon["power"]

        for armour in self.armour:
            self.protection += armour["protection"]
        if self.potion is not None:
            stats = ("protection", "power", "hp")
            for stat in stats:
                if stat in self.potion["effect"]:
                    setattr(self,
                            stat,
                            getattr(self, stat) + self.potion["effect"][stat])

    def order_determination_winner(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
