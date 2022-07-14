class Protection:

    def __init__(self, knight_p):
        self.knight_p = knight_p

    def battle_protection(self):
        total_d = {}
        knight = {}
        protect = sum([a["protection"] for a in self.knight_p["armour"]])
        knight["protection"] = protect
        if self.knight_p["potion"] is not None:
            if "protection" in self.knight_p["potion"]["effect"]:
                knight["protection"] += self.knight_p["potion"]["effect"]["protection"]
            total_d["knight_p"] = knight
        return total_d


