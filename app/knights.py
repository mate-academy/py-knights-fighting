class Warrior:

    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.protection = knight_info["protection"]

    def fight(self, other) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp < 0:
            self.hp = 0

        if other.hp < 0:
            other.hp = 0
