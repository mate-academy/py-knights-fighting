from app.knights.knights import KNIGHTS


class Inventory:
    @staticmethod
    def inventory_application(knights: KNIGHTS) -> None:
        for knight in knights:

            knight["protection"] = 0
            for armour_piece in knight["armour"]:
                knight["protection"] += armour_piece["protection"]

            knight["power"] += knight["weapon"]["power"]

            if knight["potion"] is not None:
                if "power" in knight["potion"]["effect"]:
                    knight["power"] += knight["potion"]["effect"]["power"]

                if "protection" in knight["potion"]["effect"]:
                    knight["protection"] += \
                        knight["potion"]["effect"]["protection"]

                if "hp" in knight["potion"]["effect"]:
                    knight["hp"] += knight["potion"]["effect"]["hp"]
