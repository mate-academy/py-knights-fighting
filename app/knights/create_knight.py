class KnightStatCalculator:
    def __init__(self, knights: dict) -> None:
        self.knights = knights

    def stats_knight(self) -> None:
        for key, _ in self.knights.items():
            self.knights[key]["protection"] = 0
            for armour in self.knights[key]["armour"]:
                self.knights[key]["protection"] += armour["protection"]
            self.knights[key]["power"] += self.knights[key]["weapon"]["power"]

    def apply_potion(self) -> None:
        for key, _ in self.knights.items():
            if self.knights[key]["potion"] is not None:
                if "power" in self.knights[key]["potion"]["effect"]:
                    self.knights[key]["power"] += self.knights[key]["potion"]["effect"]["power"]

                if "protection" in self.knights[key]["potion"]["effect"]:
                    self.knights[key]["protection"] += self.knights[key]["potion"]["effect"]["protection"]

                if "hp" in self.knights[key]["potion"]["effect"]:
                    self.knights[key]["hp"] += self.knights[key]["potion"]["effect"]["hp"]
