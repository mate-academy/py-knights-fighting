class Knight:
    def __init__(self, char_properties: dict) -> None:
        self.name = char_properties["name"]
        self.power = char_properties["power"]
        self.hp = char_properties["hp"]
        self.armour = char_properties["armour"]
        self.weapon = char_properties["weapon"]
        self.potion = char_properties["potion"]
        self.protection = 0

    def prepare_for_battle(self) -> None:
        for armor_element in self.armour:
            self.protection += armor_element["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
