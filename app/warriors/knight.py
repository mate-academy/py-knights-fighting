class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]
        self.potion = None
        if knight["potion"] is not None:
            self.potion = knight["potion"]
        self.protection = 0
        for armour in knight["armour"]:
            self.protection += armour["protection"]

    def potion_activate(self) -> None:
        if self.potion is not None:
            effects = self.potion["effect"]
            for key in effects:
                if key in ("power", "protection", "hp"):
                    setattr(self, key, getattr(self, key) + int(effects[key]))
