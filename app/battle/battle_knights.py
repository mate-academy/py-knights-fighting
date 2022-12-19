class Battle:

    def __init__(
            self,
            lancelot: dict,
            arthur: dict,
            mordred: dict,
            red_knight: dict
    ) -> None:

        self.lancelot = lancelot
        self.arthur = arthur
        self.mordred = mordred
        self.red_knight = red_knight

    def battle_knight(self) -> dict:

        self.lancelot["hp"] -= \
            self.mordred["power"] - self.lancelot["protection"]
        self.mordred["hp"] -= \
            self.lancelot["power"] - self.mordred["protection"]

        # check if someone fell in battle
        if self.lancelot["hp"] <= 0:
            self.lancelot["hp"] = 0

        if self.mordred["hp"] <= 0:
            self.mordred["hp"] = 0

        # 2 Arthur vs Red Knight:
        self.arthur["hp"] -= \
            self.red_knight["power"] - self.arthur["protection"]
        self.red_knight["hp"] -= \
            self.arthur["power"] - self.red_knight["protection"]

        # check if someone fell in battle
        if self.arthur["hp"] <= 0:
            self.arthur["hp"] = 0

        if self.red_knight["hp"] <= 0:
            self.red_knight["hp"] = 0

        # Return battle results:
        return {
            self.lancelot["name"]: self.lancelot["hp"],
            self.arthur["name"]: self.arthur["hp"],
            self.mordred["name"]: self.mordred["hp"],
            self.red_knight["name"]: self.red_knight["hp"],
        }
