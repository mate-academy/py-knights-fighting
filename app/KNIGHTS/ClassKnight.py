class Knight:

    """
The Knight class is designed for a simpler way of computing
battle result and store information
    """

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict | None
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.potion = potion
        # Preparation to the fight

        for item in armour:
            self.protection += item["protection"]

        # Arming

        self.power += weapon["power"]

    def using_potion(self) -> None:

        if self.potion is not None:

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
