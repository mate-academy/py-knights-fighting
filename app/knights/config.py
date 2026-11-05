class Knights:
    def __init__(self,
                 name_knight: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:

        self.name_knight = name_knight
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def equipment_knight(self) -> None:
        # , power, hp, armour, weapon, potion
        # create a new attribute - result of equipment
        self.stats = {}

        # apply armour
        self.stats["protection"] = 0
        for arm in self.armour:
            self.stats["protection"] += arm["protection"]

        # apply weapon
        self.stats["power"] = self.power + self.weapon["power"]

        # apply potion if exist
        self.stats["hp"] = self.hp
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.stats["power"] += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.stats["protection"] += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.stats["hp"] += self.potion["effect"]["hp"]
