class Potion:
    list_of_potions = []

    def __init__(self, potion: dict, owner: str) -> None:
        self.owner = owner
        self.name = potion["name"]

        if "power" in potion["effect"].keys():
            self.power = potion["effect"]["power"]
        if "hp" in potion["effect"].keys():
            self.hp = potion["effect"]["hp"]
        if "protection" in potion["effect"].keys():
            self.protection = potion["effect"]["protection"]

        Potion.list_of_potions.append(self)
