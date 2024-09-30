class Knight:
    def __init__(self, knight_stat: dict) -> None:
        self.name = knight_stat["name"]
        self.hp = knight_stat["hp"]
        self.power = knight_stat["power"] + knight_stat["weapon"]["power"]
        self.protection = self.count_protection(knight_stat)
        self.use_potion(knight_stat)

    @staticmethod
    def count_protection(knight_stat: dict) -> int:
        protection = 0
        if knight_stat.get("armour"):
            for one_part in knight_stat["armour"]:
                protection += one_part["protection"]
        return protection

    def use_potion(self, knight_stat: dict) -> None:
        if knight_stat.get("potion"):
            potion_effects = knight_stat["potion"]["effect"]

            if "hp" in potion_effects:
                self.hp += potion_effects["hp"]

            if "power" in potion_effects:
                self.power += potion_effects["power"]

            if "protection" in potion_effects:
                self.protection += potion_effects["protection"]
