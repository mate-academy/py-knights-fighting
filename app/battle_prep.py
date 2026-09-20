class BattleReady:
    def __init__(self, knight: dict) -> None:
        self.knight = knight
        knight["protection"] = 0

        # applying weaponry power
        knight["power"] += knight["weapon"]["power"]

        # applying armour protection
        if knight["armour"] == []:
            knight["protection"] = 0
        else:
            for armour_piece in knight["armour"]:
                knight["protection"] += armour_piece["protection"]

        # applying potion
        if knight["potion"] is not None:
            for name, value in knight["potion"]["effect"].items():

                if name == "power":
                    knight["power"] += value

                if name == "hp":
                    knight["hp"] += value

                if name == "protection":
                    knight["protection"] += value
