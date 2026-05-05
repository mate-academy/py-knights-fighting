from typing import Any


class Knight:

    updated_knights = {}
    knight_names = ["lancelot", "arthur", "mordred", "red_knight"]

    def __init__(self, config: Any) -> None:

        for name in Knight.knight_names:
            self.name = config[name]

            # apply armour
            self.name["protection"] = 0
            for armou in self.name["armour"]:
                self.name["protection"] += armou["protection"]

            # apply weapon
            self.name["power"] += self.name["weapon"]["power"]

            # apply potion if exist
            if self.name["potion"] is not None:
                if "power" in self.name["potion"]["effect"]:
                    self.name["power"] += (
                        self.name["potion"]["effect"]["power"]
                    )
                if "protection" in self.name["potion"]["effect"]:
                    self.name["protection"] += (
                        self.name["potion"]["effect"]["protection"]
                    )

                if "hp" in self.name["potion"]["effect"]:
                    self.name["hp"] += (
                        self.name["potion"]["effect"]["hp"]
                    )

            Knight.updated_knights[name] = self.name

    def battle(self) -> dict:
        # BATTLE:
        lancelot = Knight.updated_knights["lancelot"]
        arthur = Knight.updated_knights["arthur"]
        mordred = Knight.updated_knights["mordred"]
        red_knight = Knight.updated_knights["red_knight"]
        # 1 Lancelot vs Mordred:
        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

        # check if someone fell in battle
        if lancelot["hp"] <= 0:
            lancelot["hp"] = 0

        if mordred["hp"] <= 0:
            mordred["hp"] = 0

        # 2 Arthur vs Red Knight:
        arthur["hp"] -= red_knight["power"] - arthur["protection"]
        red_knight["hp"] -= arthur["power"] - red_knight["protection"]

        # check if someone fell in battle
        if arthur["hp"] <= 0:
            arthur["hp"] = 0

        if red_knight["hp"] <= 0:
            red_knight["hp"] = 0

        # Return battle results:
        return {
            lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
        }
