from app.knights.knight import Knight


class Preparation:

    def __init__(self, knights: dict):
        self.knights = knights

    def battle_preparation(self):
        # BATTLE PREPARATIONS:
        dict_knights = {}
        stats = ("protection", "power", "hp")

        for knight in self.knights:
            # knight
            knight = self.knights[knight]

            # apply armour
            knight["protection"] = 0
            for armour in knight["armour"]:
                knight["protection"] += armour["protection"]

            # apply weapon
            knight["power"] += knight["weapon"]["power"]

            # apply potion if exist
            if knight["potion"] is not None:

                for statistic in stats:
                    if statistic in knight["potion"]["effect"]:
                        knight[statistic] += knight["potion"]["effect"][
                            statistic
                        ]

            knight_object = Knight(knight, knight["power"], knight["hp"])
            dict_knights.update({knight_object.name["name"]: knight_object})
        return dict_knights
