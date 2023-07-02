class Knight:
    protection = 0
    list_of_knights = {}

    def __init__(self, knight: object) -> None:
        # Major values
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]

        # Adding properties to addition features
        self.search_addition_armor(knight["armour"])
        self.add_power_of_weapon(knight["weapon"])
        self.add_properties_of_potion(knight["potion"])

        # Adding all knights in the class list
        self.list_of_knights[self.name] = self

    def __repr__(self) -> str:
        return f"{self.hp}"

    def search_addition_armor(self, armor: object) -> None:
        sum_of_armor = 0

        for part in armor:
            sum_of_armor += part["protection"]

        self.protection += sum_of_armor

    def add_power_of_weapon(self, weapon: object) -> None:
        self.power += weapon["power"]

    def add_properties_of_potion(self, potion: object) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]

    def versus(self, rival: "Knight") -> None:
        self.hp -= rival.power - self.protection
        rival.hp -= self.power - rival.protection

        if self.hp <= 0:
            self.hp = 0
        elif rival.hp <= 0:
            rival.hp = 0
