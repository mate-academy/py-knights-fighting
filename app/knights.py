class Knights:

    def __init__(self, knight, config):
        self.knight = knight
        self.config = config
        self.name = self.config["name"]
        self.armour = self.config["armour"]
        self.weapon = self.config["weapon"]
        self.potion = self.config["potion"]
        self.hp = self.config["hp"]
        self.power = self.config["power"] + self.weapon["power"]
        self.protection = sum(armour["protection"] for armour in self.armour)

        stats = ("hp", "power", "protection")
        for stat in stats:
            setattr(self, stat,
                    getattr(self, stat) + (self.potion["effect"].get(stat, 0)
                                           if self.potion is not None else 0))

    def knights_fighting(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
