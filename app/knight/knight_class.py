class Knight:
    protection = 0

    def __init__(self, knight: dict) -> None:
        # Major values
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]

        # Adding properties to addition features
        self.search_addition_armor(knight["armour"])
        self.add_power_of_weapon(knight["weapon"])
        self.add_properties_of_potion(knight["potion"])

    def __repr__(self) -> str:
        return f"{self.hp}"

    def search_addition_armor(self, armor: dict) -> None:
        for part in armor:
            self.protection += part["protection"]

    def add_power_of_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def add_properties_of_potion(self, potion: dict) -> None:
        if potion is not None:
            for name, value in potion["effect"].items():
                self.power += value if name == "power" else 0
                self.protection += value if name == "protection" else 0
                self.hp += value if name == "hp" else 0

    def versus(self, rival: "Knight") -> None:
        self.hp -= rival.power - self.protection
        rival.hp -= self.power - rival.protection

        if self.hp <= 0:
            self.hp = 0
        elif rival.hp <= 0:
            rival.hp = 0
