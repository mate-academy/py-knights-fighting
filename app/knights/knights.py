class Knight:

    def __init__(self, params: dict) -> None:
        self.name = params["name"]
        self.power = params["power"]
        self.hp = params["hp"]
        self.armour = params["armour"]
        self.weapon = params["weapon"]
        self.potion = params["potion"]
        self.protection = 0
