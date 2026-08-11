class Knight:

    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.knight["protection"] = 0

    def knight_protection(self) -> None:
        for armor_element in self.knight["armour"]:
            self.knight["protection"] += armor_element["protection"]

    def knight_weapon(self) -> None:
        self.knight["power"] += self.knight["weapon"]["power"]

    def knight_potion(self) -> None:
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += (
                    self.knight["potion"]["effect"]["power"])

            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += (
                    self.knight["potion"]["effect"]["protection"])

            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]

    def battle(self, other: Knight) -> None:
        self.knight["hp"] -= other.knight["power"] - self.knight["protection"]
        other.knight["hp"] -= self.knight["power"] - other.knight["protection"]

        if self.knight["hp"] <= 0:
            self.knight["hp"] = 0

        if other.knight["hp"] <= 0:
            other.knight["hp"] = 0

    def knight_final_stats(self) -> dict:
        return {
            self.knight["name"]: self.knight["hp"]
        }
