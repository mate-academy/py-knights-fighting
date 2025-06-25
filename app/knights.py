class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list = None, weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armour is not None else []
        self.weapon = weapon if weapon is not None else {}
        self.potion = potion
        self.total_protection = 0

    def add_protection(self) -> int:
        if self.armour:
            for member in self.armour:
                self.total_protection += member["protection"]
        if self.potion and "protection" in self.potion["effect"]:
            self.total_protection += self.potion["effect"]["protection"]
        return self.total_protection

    def add_power(self) -> int:
        self.power += self.weapon["power"]
        if self.potion and "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]
        return self.power

    def add_hp(self) -> int:
        if self.potion and "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]
        return self.hp
