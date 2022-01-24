from app.knights.knight import Knight


class Preparation:

    def __init__(self, knights: dict):
        self.knights = knights

    def battle_preparation(self):
        # BATTLE PREPARATIONS:
        dict_knights = {}
        for knight in self.knights:
            # knight
            knight = self.knights[knight]

            # apply armour
            knight["protection"] = 0
            for a in knight["armour"]:
                knight["protection"] += a["protection"]

            # apply weapon
            knight["power"] += knight["weapon"]["power"]

            # apply potion if exist
            if knight["potion"] is not None:
                if "power" in knight["potion"]["effect"]:
                    knight["power"] += knight["potion"]["effect"]["power"]

                if "protection" in knight["potion"]["effect"]:
                    knight["protection"] +=\
                        knight["potion"]["effect"]["protection"]

                if "hp" in knight["potion"]["effect"]:
                    knight["hp"] += knight["potion"]["effect"]["hp"]

            knight_object = Knight(knight, knight["power"], knight["hp"])
            dict_knights.update({knight_object.name["name"]: knight_object})
        return dict_knights
