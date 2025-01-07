class Knight:
    def __init__(self, data_dict: dict) -> None:
        self. name = data_dict["name"]
        self.power = data_dict["power"] + data_dict["weapon"]["power"]
        self.hp = data_dict["hp"]
        self.potion = data_dict["potion"]
        self.protection = self.armour_score(data_dict["armour"])
        if data_dict["potion"] is not None:
            self.potion_effect(data_dict["potion"]["effect"])

    @staticmethod
    def armour_score(list_of_armor: list) -> int:
        """Count armour score """
        result = 0
        for part_of_armour in list_of_armor:
            if "protection" in part_of_armour:
                result += part_of_armour["protection"]
            else:
                raise ValueError(f"Missing 'protection'"
                                 f" key in {part_of_armour}")
        return result

    def potion_effect(self, potion: dict) -> None:
        """ Use potion effects"""
        if potion.get("hp"):
            self.hp += potion["hp"]
        if potion.get("power"):
            self.power += potion["power"]
        if potion.get("protection"):
            self.protection += potion["protection"]
