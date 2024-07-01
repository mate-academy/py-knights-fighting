class Knight:
    def __init__(self, knights: dict) -> None:
        self.name = knights["name"]
        self.power = knights["power"]
        self.hp = knights["hp"]
        self.armour = knights["armour"]
        self.weapon = knights["weapon"]
        self.potion = knights["potion"]
        self.protection = 0
