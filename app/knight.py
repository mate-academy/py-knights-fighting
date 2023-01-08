class Knight:
    """Class makes the knight instances and necessary methods"""

    def __init__(self, name: str, power: int, hp: int) -> None:
        """Method adds basic knight parameters"""
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_armour(self, armour: list[dict]) -> None:
        """Method adds armour protection to the knight"""
        total_protection = 0
        for part in armour:
            total_protection += part["protection"]
        self.protection = total_protection

    def get_weapon(self, weapon: dict) -> None:
        """Method adds the power of knight's weapon"""
        self.power += weapon["power"]

    def get_potion(self, potion: dict) -> None:
        """Method adds potion effect to the knight"""
        if potion is not None:
            # ingredients = potion["effect"]
            self.power += potion["effect"]["power"]
            self.hp += potion["effect"]["hp"]
            self.protection += potion["effect"]["protection"]


