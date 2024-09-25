class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    def calculate_param(self, knight: dict) -> None:

        # apply armour
        for armor in knight["armour"]:
            self.protection += armor["protection"]

        # apply weapon
        self.power += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                self.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                self.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                self.hp += knight["potion"]["effect"]["hp"]
