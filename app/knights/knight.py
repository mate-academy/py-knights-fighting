class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = None,
                 weapon: dict = None,
                 potion: dict = None
                 ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0
        self.hp = 0

    def get_protection(self) -> None:
        self.protection = 0
        if self.armour is not None:
            for armour in self.armour:
                self.protection += armour["protection"]
        if self.potion is not None:
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def get_power(self) -> None:
        self.power += self.base_power
        if self.weapon is not None:
            self.power += self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

    def get_hp(self) -> None:
        self.hp += self.base_hp
        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
