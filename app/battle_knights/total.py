from app.battle_knights.knights_dict import knights


class Total:

    def __init__(self, dict_knights=knights):
        self.dict_knights = dict_knights

    def battle_hp(self):
        for knight_person in self.dict_knights.values():
            if knight_person["potion"] is not None:
                if "hp" in knight_person["potion"]["effect"]:
                    knight_person["hp"] += knight_person["potion"]["effect"]["hp"]
            return knight_person["hp"]
