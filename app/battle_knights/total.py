class Total:

    def __init__(self, knight):
        self.knight = knight

    def battle_hp(self):
        # BATTLE PREPARATIONS:

        if self.knight["potion"] is not None:
            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
        return self.knight["hp"]
