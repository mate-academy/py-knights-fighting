class Knight:
    def __init__(self, data_dict: dict) -> None:
        self. name = data_dict["name"]
        self.power = data_dict["power"] + data_dict["weapon"]["power"]
        self.hp = data_dict["hp"]
        self.potion = data_dict["potion"]
        self.protection = self.count_armour_score(data_dict["armour"])
        if data_dict["potion"] is not None:
            self.use_potion_effect(data_dict["potion"]["effect"])

    @staticmethod
    def count_armour_score(list_of_armor: list) -> int:
        try:
            return sum(part["protection"] for part in list_of_armor)
        except KeyError as e:
            raise ValueError(f"Missing 'protection' key in one of the armor parts: {e}")

    def use_potion_effect(self, potion: dict) -> None:
        if potion.get("hp"):
            self.hp += potion["hp"]
        if potion.get("power"):
            self.power += potion["power"]
        if potion.get("protection"):
            self.protection += potion["protection"]
