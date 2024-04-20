class Potion:
    def __init__(self, name: str, potion_info: dict) -> None:
        self.name = name
        self.power = 0
        self.protection = 0
        self.hp = 0

        if "power" in potion_info:
            self.power = potion_info["power"]

        if "protection" in potion_info:
            self.protection = potion_info["protection"]

        if "hp" in potion_info:
            self.hp = potion_info["hp"]
