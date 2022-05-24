class Knight:
    def __init__(self, knight: dict):
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def battle_preparation(self):
        # apply armour
        stats = ["power", "protection", "hp"]
        for armour in self.armour:
            self.protection += armour["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            for stat in stats:
                if stat in self.potion["effect"]:
                    value = getattr(self, stat) + self.potion["effect"][stat]
                    setattr(self, stat, value)

    def start_battle(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0
