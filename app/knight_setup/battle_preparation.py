class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.knight_data = knight_data
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.protection = 0
        self.hp = knight_data["hp"]

        self.add_prot()
        self.add_weapon()
        self.use_potions()

    def add_prot(self) -> None:
        for part in self.knight_data["armour"]:
            self.protection += part["protection"]

    def add_weapon(self) -> None:
        self.power += self.knight_data["weapon"]["power"]

    def use_potions(self) -> None:
        potion = self.knight_data["potion"]
        reactions = {"power": 0, "protection": 0, "hp": 0}
        if potion:
            for reaction in reactions.keys():
                if reaction in potion["effect"]:
                    reactions[reaction] += potion["effect"][reaction]
            self.power += reactions["power"]
            self.protection += reactions["protection"]
            self.hp += reactions["hp"]
