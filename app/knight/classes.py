class Knight:
    knights: list[Knight] = []

    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]
        self.protection = 0
        self.power = knight_dict["weapon"]["power"] + knight_dict["power"]
        self.hp = knight_dict["hp"]
        if knight_dict["potion"] is not None:
            knight_potion = knight_dict["potion"]
            if "hp" in knight_potion["effect"]:
                self.hp += knight_potion["effect"]["hp"]
            if "protection" in knight_potion["effect"]:
                self.protection += knight_potion["effect"]["protection"]
            if "power" in knight_potion["effect"]:
                self.power += knight_dict["potion"]["effect"]["power"]
        if knight_dict["armour"] is not None:
            for element in knight_dict["armour"]:
                self.protection += element["protection"]
        Knight.knights.append(self)

    def match(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
