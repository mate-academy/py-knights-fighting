class Potion:
    def __init__(self, potion: dict):
        self.potion = potion

    def use_potion(self, knight):
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                knight.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                knight.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                knight.hp += self.potion["effect"]["hp"]
