class Knight:
    def __init__(self, dict_knight: dict) -> None:
        self.name = dict_knight["name"]
        self.hp = dict_knight["hp"]
        self.power = dict_knight["power"] + dict_knight["weapon"]["power"]
        self.protection = sum(
            [armour["protection"] for armour in dict_knight["armour"]]
        )
        self.drink_the_potion(dict_knight["potion"])

    def drink_the_potion(self, potion: dict) -> None:
        if potion is not None:
            effects = {
                "power": self.power,
                "protection": self.protection,
                "hp": self.hp,
            }
            for effect in effects:
                if effect in potion["effect"]:
                    setattr(
                        self,
                        effect,
                        effects[effect] + potion["effect"][effect],
                    )
