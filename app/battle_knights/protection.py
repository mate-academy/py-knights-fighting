from app.battle_knights.knights_dict import knights


class Protection:

    def __init__(self, people_dict=knights):
        self.people_dict = people_dict

    def battle_protection(self):
        for knight_p in self.people_dict.values():
            protect = sum([a["protection"] for a in knight_p["armour"]])
            if knight_p["potion"] is not None:
                if "protect" in knight_p["potion"]["effect"]:
                    protect += knight_p["potion"]["effect"]["protection"]
            return protect

