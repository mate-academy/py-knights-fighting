class Knight:
    def __init__(self, name: str, config: dict) -> None:
        self.knight = config[name]
        self._apply()

    def _apply(self) -> None:
        # apply armour
        self.knight["protection"] = 0
        for armour in self.knight["armour"]:
            self.knight["protection"] += armour["protection"]

        # apply weapon
        self.knight["power"] += self.knight["weapon"]["power"]

        # apply potion if exist
        potion = self.knight["potion"]
        if potion is not None:
            if "power" in potion["effect"]:
                self.knight["power"] += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.knight["protection"] += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.knight["hp"] += potion["effect"]["hp"]
