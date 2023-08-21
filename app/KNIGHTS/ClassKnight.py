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

        # Preparation to the fight

        for item in armour:
            self.protection += item["protection"]

        # Arming

        self.power += weapon["power"]

        # Using potion

        if potion is not None:

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
