class Battle:
    def __init__(self, knights: dict) -> None:
        self.knights = knights

    def start_battle(self) -> dict:
        lancelot = self.knights["lancelot"]
        mordred = self.knights["mordred"]
        arthur = self.knights["arthur"]
        red_knight = self.knights["red_knight"]

        # 1 Lancelot vs Mordred:
        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

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
