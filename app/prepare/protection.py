class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_armour(self, armour: list):
        if armour:
            for part in armour:
                if "protection" in part:
                    self.protection += part["protection"]

    def get_weapon(self, weapon: dict):
        self.power += weapon["power"]

    def get_potion(self, potion: dict):
        if potion is not None:
            stats = ("protection", "power", "hp")
            for stat in stats:
                if stat in potion["effect"]:
                    setattr(self,
                            stat,
                            getattr(self, stat) + potion["effect"][stat])
