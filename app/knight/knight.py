class Knight:
    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.name = knight["name"]
        self.hp = self.knight["hp"]
        self.power = knight["power"] + knight["weapon"]["power"]
        self.protection = self.get_protection()
        self.use_potion()

    def get_protection(self) -> int:
        if not self.knight["armour"]:
            return 0
        return sum([armour["protection"] for armour in self.knight["armour"]])

    def use_potion(self) -> None:
        potion = self.knight["potion"]
        if potion is None:
            return
        for effect_name, effect_value in potion["effect"].items():
            if effect_name == "power":
                self.power += effect_value
            elif effect_name == "hp":
                self.hp += effect_value
            elif effect_name == "protection":
                self.protection += effect_value
