class Knights:
    def __init__(self, knights: object) -> None:
        self.knights = knights

    def knight_kingdom(self, kingdom: str) -> dict:
        knight = self.knights[kingdom]
        knight["protection"] = 0
        for part in knight["armour"]:
            knight["protection"] += part["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += \
                    knight["potion"]["effect"]["protection"]

            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
        return knight
