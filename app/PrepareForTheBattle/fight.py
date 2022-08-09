class Attributes:
    def __init__(self, knights):
        self.lancelot = knights["lancelot"]
        self.arthur = knights["arthur"]
        self.mordred = knights["mordred"]
        self.red_knight = knights["red_knight"]
        self.result = {}

    def knights_battle(self):
        self.lancelot["hp"] -= self.mordred["power"] - self.lancelot["armor"]
        if self.lancelot["hp"] <= 0:
            self.result["Lancelot"] = 0
        else:
            self.result["Lancelot"] = self.lancelot["hp"]

        self.arthur["hp"] -= self.red_knight["power"] - self.arthur["armor"]
        if self.arthur["hp"] <= 0:
            self.result["Artur"] = 0
        else:
            self.result["Artur"] = self.arthur["hp"]

        self.mordred["hp"] -= self.lancelot["power"] - self.mordred["armor"]
        if self.mordred["hp"] <= 0:
            self.result["Mordred"] = 0
        else:
            self.result["Mordred"] = self.mordred["hp"]

        self.red_knight["hp"] -= \
            self.arthur["power"] - self.red_knight["armor"]
        if self.red_knight["hp"] <= 0:
            self.result["Red Knight"] = 0
        else:
            self.result["Red Knight"] = self.red_knight["hp"]

        return self.result
