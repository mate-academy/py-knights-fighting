class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.protect = 0
        self.apply_armour(knight_data["armour"])
        self.apply_weapon(knight_data["weapon"])
        self.apply_potion(knight_data["potion"])

    def apply_armour(self, armour_dict: dict) -> None:
        for armour in armour_dict:
            self.protect += armour["protection"]

    def apply_weapon(self, weapon_dict: dict) -> None:
        self.power += weapon_dict["power"]

    def apply_potion(self, potion_dict: dict) -> None:
        if potion_dict is not None:
            effect = potion_dict["effect"]
            if "hp" in effect:
                self.hp += effect["hp"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protect += effect["protection"]
