class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def battle_preparations(self) -> None:
        for part_of_armour in self.armour:
            self.protection += part_of_armour["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            # I used if method because if I do it with loops like
            # for baff in self.potion["effect"]
            # then I won't be able to write self.baff
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0
