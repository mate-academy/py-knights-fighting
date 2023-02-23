class Knight:
    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.power = info["power"]
        self.hp = info["hp"]
        self.protection = 0
        self.preparing(info)

    def preparing(self, info: dict) -> None:
        self.power += info["weapon"]["power"]

        if info["armour"]:
            for part in info["armour"]:
                self.protection += part["protection"]

        if info["potion"] is not None:
            for effect in info["potion"]["effect"]:
                self.__dict__[effect] += (
                    info["potion"]["effect"].get(effect, 0)
                )
