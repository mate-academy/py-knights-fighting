class Fight:
    def __init__(self, knights: list) -> None:
        self.knights = knights

    def fight(self) -> dict:
        for knight in self.knights:
            red_knight_stats["hp"] -= x_knight_stats["power"] - red_knight_stats["protection"]
            x_knight_stats["hp"] -= red_knight_stats["power"] - x_knight_stats["protection"]

        if arthur["hp"] <= 0:
            arthur["hp"] = 0

        if red_knight["hp"] <= 0:
            red_knight["hp"] = 0

        return {
            lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
        }