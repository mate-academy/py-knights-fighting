class Knight:
    def __init__(self, knight_data: dict) -> None:
        # Базові стати
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"] + knight_data["weapon"]["power"]
        self.protection = 0

        # Додаємо зілля (якщо є)
        if knight_data.get("potion"):
            effect = knight_data["potion"]["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "protection" in effect:
                self.protection += effect["protection"]

        # Рахуємо захист від броні
        for armor_piece in knight_data.get("armour", []):
            self.protection += armor_piece["protection"]
