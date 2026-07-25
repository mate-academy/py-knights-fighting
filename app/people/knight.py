class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]

        self.protection = sum(
            armour["protection"]
            for armour in data["armour"]
        )

        self.power += data["weapon"]["power"]

        potion = data["potion"]

        if potion:
            effects = potion["effect"]

            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
