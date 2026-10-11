class Knights:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.hp = knight_config["hp"]
        self.power = knight_config["power"]
        self.protection = 0

        self.apply_armour(knight_config["armour"])
        self.apply_weapon(knight_config["weapon"])
        self.apply_potion(knight_config["potion"])

    def apply_armour(self, armour_list: list) -> None:
        for armour in armour_list:
            self.protection += armour["protection"]

    def apply_weapon(self, weapon_dict: dict) -> None:
        self.power += weapon_dict["power"]

    def apply_potion(self, potion_dict: dict | None) -> None:
        if potion_dict is not None:
            effect = potion_dict["effect"]
            for stat, value in effect.items():
                if stat == "hp":
                    self.hp += value
                elif stat == "power":
                    self.power += value
                elif stat == "protection":
                    self.protection += value
