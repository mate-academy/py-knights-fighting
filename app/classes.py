class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.final_hp = self.calculate_final_hp()
        self.final_protection = self.calculate_final_protection()
        self.final_power = self.calculate_final_power()

    def calculate_final_hp(self) -> int:
        hp = self.hp
        if self.potion and "hp" in self.potion["effect"]:
            hp += self.potion["effect"]["hp"]
        return hp

    def calculate_final_protection(self) -> int:
        protection = 0
        for item in self.armour:
            protection += item["protection"]

        if self.potion and "protection" in self.potion["effect"]:
            protection += self.potion["effect"]["protection"]
        return protection

    def calculate_final_power(self) -> int:
        power = self.power + self.weapon["power"]
        if self.potion and "power" in self.potion["effect"]:
            power += self.potion["effect"]["power"]
        return power
