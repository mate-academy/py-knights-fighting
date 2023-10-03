class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"] + knight["weapon"].get("power", 0)
        self.protection = sum(arm["protection"] for arm in knight["armour"])

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]

    @staticmethod
    def battle_with_enemy(knight1: "Knight", knight2: "Knight") -> None:
        knight1.hp = max(0, knight1.hp - (knight2.power - knight1.protection))
        knight2.hp = max(0, knight2.hp - (knight1.power - knight2.protection))
