class Knights:

    def __init__(self, knight, config):
        self.knight = knight
        self.config = config
        self.name = self.config["name"]
        self.hp = self.config["hp"] + \
            (self.config["potion"]["effect"].get("hp", 0)
                if self.config["potion"] is not None else 0)
        self.power = self.config["power"] + self.config["weapon"]["power"] + \
            (self.config["potion"]["effect"].get("power", 0)
                if self.config["potion"] is not None else 0)
        self.protection = sum(armour["protection"] for armour
                              in self.config["armour"]) + \
            (self.config["potion"]["effect"].get("protection", 0)
                if self.config["potion"] is not None else 0)

    def knights_fighting(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
