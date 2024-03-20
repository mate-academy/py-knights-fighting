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
            for effect, value in self.potion["effect"].items():
                if hasattr(self, effect):
                    current_value = getattr(self, effect)
                    setattr(self, effect, current_value + int(value))
