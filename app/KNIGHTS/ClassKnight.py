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
        effects_list = ["protection", "power", "hp"]
        status = [self.protection, self.power, self.hp]
        if self.potion:

            for i in range(len(effects_list)):

                if effects_list[i] in self.potion["effect"]:
                    status[i] += self.potion["effect"][effects_list[i]]

        self.protection = status[0]
        self.power = status[1]
        self.hp = status[2]
