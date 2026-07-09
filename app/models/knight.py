class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.protection = 0

        for armour_part in knight_data["armour"]:
            self.protection += armour_part["protection"]

        self.power += knight_data["weapon"]["power"]

        if knight_data["potion"] is not None:
            potion_effect = knight_data["potion"]["effect"]
            self.power += potion_effect.get("power", 0)
            self.protection += potion_effect.get("protection", 0)
            self.hp += potion_effect.get("hp", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0
