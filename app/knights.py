class Knight:
    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary["name"]
        self.power = dictionary["power"]
        self.hp = dictionary["hp"]
        self.armour = dictionary["armour"]
        self.weapon = dictionary["weapon"]
        self.potion = dictionary["potion"]

    def prepare_for_battle(self) -> None:
        self.protection = 0
        for armour_things in self.armour:
            self.protection += armour_things["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
