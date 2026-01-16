class Knight:
    def __init__(self, knight_dict: dict) -> None:
        # Init knight
        self.name = knight_dict["name"]
        self.protection = 0
        self.power = knight_dict["power"]
        self.hp = knight_dict["hp"]

        # Add armors
        for item in knight_dict["armour"]:
            self.protection += item["protection"]

        # Add weapons
        self.power += knight_dict["weapon"]["power"]

        # Add potion
        if knight_dict["potion"] is not None:
            effect_values = knight_dict["potion"]["effect"]
            if "power" in effect_values:
                self.power += effect_values["power"]
            if "protection" in effect_values:
                self.protection += effect_values["protection"]
            if "hp" in effect_values:
                self.hp += effect_values["hp"]

    def __str__(self) -> str:
        return f"Knight name: {self.name}"

    def take_hit(self, power: int) -> None:
        new_hp = self.hp - (power - self.protection)
        self.hp = 0 if new_hp <= 0 else new_hp
