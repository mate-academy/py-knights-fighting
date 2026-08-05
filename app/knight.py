class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name: str = knight_data["name"]
        self.hp: int = knight_data["hp"]
        self.power: int = knight_data["power"]
        self.protection: int = 0

        for armour in knight_data["armour"]:
            self.protection += armour["protection"]

        self.power += knight_data["weapon"]["power"]

        if knight_data["potion"] is not None:
            effect = knight_data["potion"]["effect"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]

    def take_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection

        if self.hp <= 0:
            self.hp = 0
