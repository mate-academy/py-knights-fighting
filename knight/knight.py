class Knight:

    def __init__(self, knight: dict):
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.armour = []
        self.potion = {}
        self.weapon = {}
        for arm in knight["armour"]:
            self.add_armour(arm["part"], arm["protection"])
        self.add_weapon(knight["weapon"])
        self.add_potion(knight["potion"])

    def add_armour(self, name: str, protection: int):
        self.armour.append({"part": name, "protection": protection})
        self.protection += protection

    def add_weapon(self, weapon: dict):
        self.weapon["name"] = weapon["name"]
        self.weapon["power"] = weapon["power"]
        self.power += weapon["power"]

    def add_potion(self, potion: dict):
        if potion is not None:
            self.potion["name"] = potion["name"]
            self.potion["effect"] = potion["effect"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]
