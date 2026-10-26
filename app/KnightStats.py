class Knight:

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]

        self.protection = 0
        if data["armour"]:
            for arm in data["armour"]:
                self.protection += arm["protection"]

        self.power += data["weapon"]["power"]

        if data["potion"] is not None:
            if "power" in data["potion"]["effect"]:
                self.power += data["potion"]["effect"]["power"]
            if "hp" in data["potion"]["effect"]:
                self.hp += data["potion"]["effect"]["hp"]
            if "protection" in data["potion"]["effect"]:
                self.protection += data["potion"]["effect"]["protection"]
