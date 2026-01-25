class Knight():
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.armour = knight_info["armour"]
        self.weapon = knight_info["weapon"]
        self.potion = knight_info["potion"]

    def knights_stats(self) -> dict:
        ammount_of_protection = 0
        ammount_of_hp = self.hp
        ammount_of_power = self.power + self.weapon["power"]

        if self.armour:
            for armor_part in self.armour:
                ammount_of_protection += armor_part["protection"]

        if self.potion:
            if "protection" in self.potion["effect"]:
                ammount_of_protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                ammount_of_hp = (self.hp
                                 + self.potion["effect"]["hp"]
                                 )
            if "power" in self.potion["effect"]:
                ammount_of_power = (self.power
                                    + self.weapon["power"]
                                    + self.potion["effect"]["power"]
                                    )

        return {
            "hp": ammount_of_hp,
            "power": ammount_of_power,
            "protection": ammount_of_protection
        }
