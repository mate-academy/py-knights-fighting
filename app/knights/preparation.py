class Knight:
    def __init__(self, knight_and_amo: dict):
        self.name = knight_and_amo["name"]
        self.power = knight_and_amo["power"]
        self.hp = knight_and_amo["hp"]
        self.dr = 0

        for a in knight_and_amo["armour"]:
            self.dr += a["protection"]
        self.power += knight_and_amo["weapon"]["power"]
        if knight_and_amo["potion"] is not None:
            if "power" in knight_and_amo["potion"]["effect"]:
                self.power += knight_and_amo["potion"]["effect"]["power"]

            if "protection" in knight_and_amo["potion"]["effect"]:
                self.dr += knight_and_amo["potion"]["effect"]["protection"]

            if "hp" in knight_and_amo["potion"]["effect"]:
                self.hp += knight_and_amo["potion"]["effect"]["hp"]

