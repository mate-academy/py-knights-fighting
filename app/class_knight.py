class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def knight_puts_on_armor(self) -> int | None:
        if self.armour == []:
            return
        for element_armor in self.armour:
            self.protection += element_armor["protection"]
        return self.protection

    def knight_takes_weapon(self) -> None:
        self.power += self.weapon["power"]

    def knight_drinks_the_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
