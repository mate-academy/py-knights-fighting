class Potion:
    def __init__(self, potion: dict) -> None:
        self.effect = potion["effect"]

    def apply_potion(self, knight: callable) -> None:
        """apply potion if exist"""
        if "power" in self.effect:
            knight.power += self.effect["power"]

        if "protection" in self.effect:
            knight.protection += self.effect["protection"]

        if "hp" in self.effect:
            knight.hp += self.effect["hp"]
