class Knight:

    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def armour(self, armour: list):
        for a in armour:
            self.protection += a["protection"]

    def weapon(self, weapon: dict):
        self.power += weapon["power"]

    def potion(self, potion: dict):
        if potion is not None:
            stats = ("protection", "power", "hp")
            for stat in stats:
                if potion["effect"].get(stat):
                    setattr(self, stat,
                            getattr(self, stat) + potion["effect"][stat])
