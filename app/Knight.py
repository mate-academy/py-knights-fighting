class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"] + knight_data["weapon"]["power"]
        self.protection = sum(
            armour_part["protection"]
            for armour_part in knight_data["armour"]
        )

        if knight_data["potion"]:
            effects = knight_data["potion"]["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def __str__(self) -> str:
        return (f"{self.name} (HP: {self.hp},"
                f" Power: {self.power}, Protection: {self.protection})")

    @classmethod
    def get_knight(cls, knight: dict) -> Knight:
        return Knight(knight)
