class Knight:
    """Class creates the knight instance and necessary methods"""

    def __init__(self, name: str, knight: dict) -> None:
        """Method constructs knight instance"""
        self.name = knight[name]["name"]
        self.power = knight[name]["power"]
        self.hp = knight[name]["hp"]
        self.armour = knight[name]["armour"]
        self.weapon = knight[name]["weapon"]
        self.potion = knight[name]["potion"]
        self.protection = 0

    def get_armour(self) -> None:
        """Method adds armour protection to the knight"""
        total_protection = 0
        for part in self.armour:
            total_protection += part["protection"]
        self.protection = total_protection

    def get_weapon(self) -> None:
        """Method adds the power of knight's weapon"""
        self.power += self.weapon["power"]

    def get_potion(self) -> None:
        """Method adds potion effect to the knight"""
        values = ["power", "protection", "hp"]
        if self.potion is not None:
            for value in values:
                if value in self.potion["effect"]:
                    setattr(
                        self,
                        value,
                        (getattr(self, value) + self.potion["effect"][value])
                    )
