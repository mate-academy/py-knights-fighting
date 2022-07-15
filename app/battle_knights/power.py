class Power:

    def __init__(self, knight_people):
        self.knight_people = knight_people

    def battle_power(self):
        total_dic = {}
        self.knight_people["power"] += self.knight_people["weapon"]["power"]
        if self.knight_people["potion"] is not None:
            if "power" in self.knight_people["potion"]["effect"]:
                self.knight_people["power"] +=\
                    self.knight_people["potion"]["effect"]["power"]
        total_dic["power"] = self.knight_people["power"]
        return total_dic
