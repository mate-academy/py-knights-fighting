class Knight:
    def __init__(self, knights: dict) -> None:
        self.name = knights["name"]
        self.power = knights["power"]
        self.hp = knights["hp"]
        self.protection = 0
        self.armour = knights["armour"]
        self.weapon = knights["weapon"]
        self.potion = knights["potion"]

    def battle_match(self, other: "Knight") -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0
