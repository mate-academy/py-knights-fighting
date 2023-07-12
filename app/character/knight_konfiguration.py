class Character:
    def __init__(self, name: str, data_knight: dict) -> None:
        self.name = name
        self.hp = data_knight[name]["hp"]
        self.protection = 0
        self.power = data_knight[name]["power"]

        for a in data_knight[name]["armour"]:
            self.protection += a["protection"]

        self.power += data_knight[name]["weapon"]["power"]

        if data_knight[name]["potion"] is not None:
            if "power" in data_knight[name]["potion"]["effect"]:
                self.power += data_knight[name]["potion"]["effect"]["power"]

            if "protection" in data_knight[name]["potion"]["effect"]:
                self.protection += \
                    data_knight[name]["potion"]["effect"]["protection"]

            if "hp" in data_knight[name]["potion"]["effect"]:
                self.hp += data_knight[name]["potion"]["effect"]["hp"]
