class PrepareKnight:
    def __init__(self, knights_dict: dict) -> None:
        self.knights_dict = knights_dict.copy()
        self.prepare_knight_for_battle()

    def get_prepared_knight(self, knight_name: str) -> dict:
        return self.knights_dict[knight_name]

    def prepare_knight_for_battle(self) -> dict:
        for _, knight in self.knights_dict.items():
            knight["protection"] = 0
            self.wear_armor(knight)
            knight["power"] += knight["weapon"]["power"]
            self.apply_potions(knight_potion=knight["potion"], knight=knight)
        return self.knights_dict

    @staticmethod
    def wear_armor(knight: dict) -> None:
        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

    @staticmethod
    def apply_potions(knight_potion: dict, knight: dict) -> None:
        if knight_potion is not None:
            if "power" in knight_potion["effect"]:
                knight["power"] += knight_potion["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += knight_potion["effect"]["protection"]

            if "hp" in knight_potion["effect"]:
                knight["hp"] += knight_potion["effect"]["hp"]
