class Armour:
    def __init__(self, parts: list[dict]) -> None:
        self.helmet_protection = 0
        self.breastplate_protection = 0
        self.boots_protection = 0

        for part in parts:
            if part["part"] == "helmet":
                self.helmet_protection = part["protection"]
            if part["part"] == "breastplate":
                self.breastplate_protection = part["protection"]
            if part["part"] == "boots":
                self.boots_protection = part["protection"]
