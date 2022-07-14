class Total:

    def __init__(self, knight_person):
        self.knight_person = knight_person

    def battle_hp(self):
        totali = {}
        if self.knight_person["potion"] is not None:
            if "hp" in self.knight_person["potion"]["effect"]:
                self.knight_person["hp"] += self.knight_person["potion"]["effect"]["hp"]
            totali["knight_person"] = {"hp": self.knight_person["hp"]}
        return totali


