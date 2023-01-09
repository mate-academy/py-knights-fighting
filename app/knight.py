class Knight:
    """Class creates the knight instance and necessary methods"""

    def __init__(self, name: str, knights: dict) -> None:
        """Method constructs knight instance"""
        self.name = name
        self.real_name = knights[name]["name"]
        self.power = knights[name]["power"]
        self.hp = knights[name]["hp"]
        self.armour = knights[name]["armour"]
        self.weapon = knights[name]["weapon"]
        self.potion = knights[name]["potion"]
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
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
