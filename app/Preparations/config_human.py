class Knight:
    def __init__(self, human: dict) -> None:
        self.human = human

    def change_config(self) -> dict:
        # apply armour
        for name in self.human:
            knight = self.human[name]
            knight["protection"] = 0

            for value in knight["armour"]:
                knight["protection"] += value["protection"]

            knight["power"] += knight["weapon"]["power"]

            if knight["potion"] is not None:
                if "power" in knight["potion"]["effect"]:
                    knight["power"] += knight["potion"]["effect"]["power"]

                if "protection" in knight["potion"]["effect"]:
                    knight["protection"] += (
                        knight["potion"]["effect"]["protection"]
                    )

                if "hp" in knight["potion"]["effect"]:
                    knight["hp"] += knight["potion"]["effect"]["hp"]
        dict_knights = {
            "lancelot": self.human["lancelot"],
            "arthur": self.human["arthur"],
            "mordred": self.human["mordred"],
            "red_knight": self.human["red_knight"]
        }
        return dict_knights
