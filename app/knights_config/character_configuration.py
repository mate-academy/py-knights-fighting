class Character:

    def __init__(self, name_knight: str, knight: dict) -> None:
        self.name_knight = name_knight
        self.knight = knight

    def new_character(self) -> dict:
        hero = self.knight[self.name_knight]

        # apply armour
        hero["protection"] = 0
        for armour in hero["armour"]:
            hero["protection"] += armour["protection"]

        # apply weapon
        hero["power"] += hero["weapon"]["power"]

        # apply potion if exist
        if hero["potion"] is not None:
            if "power" in hero["potion"]["effect"]:
                hero["power"] += hero["potion"]["effect"]["power"]

            if "protection" in hero["potion"]["effect"]:
                hero["protection"] += hero["potion"]["effect"]["protection"]

            if "hp" in hero["potion"]["effect"]:
                hero["hp"] += hero["potion"]["effect"]["hp"]
        return hero
