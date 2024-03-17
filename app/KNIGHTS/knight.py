class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]
        self.potion = None
        if knight["potion"] is not None:
            self.potion = knight["potion"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0
        for armour in knight["armour"]:
            self.protection += armour["protection"]

    def potion_activate(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += int(self.potion["effect"]["power"])

            if "protection" in self.potion["effect"]:
                self.protection += int(self.potion["effect"]["protection"])

            if "hp" in self.potion["effect"]:
                self.hp += int(self.potion["effect"]["hp"])
        if self.potion is None:
            return None
        self.power += self.potion["effect"]["power"]
        self.hp += self.potion["effect"]["hp"]
        if len(self.potion["effect"]) == 3:
            self.protection += self.potion["effect"]["protection"]
