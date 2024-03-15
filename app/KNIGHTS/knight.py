class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0
        for armour in knight["armour"]:
            self.protection += armour["protection"]

    def potion_activate(self) -> None:
        if self.potion is None:
            return None
        self.power += self.potion["effect"]["power"]
        self.hp += self.potion["effect"]["hp"]
        if len(self.potion["effect"]) == 3:
            self.protection += self.potion["effect"]["protection"]
