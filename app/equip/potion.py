class Potion:
    def __init__(self, potion: dict):
        self.potion = potion

    def get_potion(self, hero) -> None:
        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                hero.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                hero.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                hero.protection += self.potion["effect"]["protection"]
