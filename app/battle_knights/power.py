from app.battle_knights.knights_dict import knights


class Power:

    def __init__(self, knights_person=knights):
        self.knights_person = knights_person

    def battle_power(self):
        for knight_people in self.knights_person.values():
            knight_people["power"] += knight_people["weapon"]["power"]
            if knight_people["potion"] is not None:
                if "power" in knight_people["potion"]["effect"]:
                    knight_people["power"] += knight_people["potion"]["effect"]["power"]
            return knight_people["power"]
