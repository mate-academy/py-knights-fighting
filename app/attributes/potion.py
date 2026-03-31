class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion['name']
        self.effect = potion['effect']

    def use_potion(self, knight) -> None:
        if "power" in self.effect:
            knight.power += self.effect['power']
        if "hp" in self.effect:
            knight.hp += self.effect['hp']
        if "protection" in self.effect:
            knight.protection += self.effect['protection']
