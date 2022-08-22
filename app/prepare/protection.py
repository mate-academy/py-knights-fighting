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
            if "effect" in potion:
                for effect in potion["effect"].keys():
                    if effect == "power":
                        self.power += potion["effect"]["power"]
                    elif effect in "hp":
                        self.hp += potion["effect"]["hp"]
                    elif effect == "protection":
                        self.protection += potion["effect"]["protection"]
