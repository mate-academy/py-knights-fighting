class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.prepare(
            armour=knight_data["armour"],
            weapon=knight_data["weapon"],
            potion=knight_data["potion"],
        )

    def prepare(self, armour: list, weapon: dict, potion: dict | None) -> None:
        self.protection = sum(item["protection"] for item in armour)
        self.power += weapon["power"]

        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
