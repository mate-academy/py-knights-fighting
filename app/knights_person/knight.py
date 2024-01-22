class Knight:

    def __init__(self, knight_stats: dict) -> None:
        self.name = knight_stats["name"]
        self.power = knight_stats["power"]
        self.hp = knight_stats["hp"]
        self.armour: list[dict] = knight_stats["armour"]
        self.weapon: dict = knight_stats["weapon"]
        self.potion: dict = knight_stats["potion"]
        self.protection = 0

    def preparations(self) -> None:

        # apply armour
        for arm in self.armour:
            self.protection += arm["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
