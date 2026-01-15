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
                for effect in self.knights[key]["potion"]["effect"].keys():
                    if effect in self.knights[key]["potion"]["effect"]:
                        self.knights[key][effect] += self.knights[key]["potion"]["effect"][effect]
