class Knight:
    knights = []

    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        Knight.knights.append(self)

    def calculate_power(self) -> int:
        result_power = self.power + self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                result_power += self.potion["effect"]["power"]
        return result_power

    def calculate_hp(self) -> int:
        result_hp = self.hp
        if self.potion is not None:
            if "hp" in self.potion["effect"]:
                result_hp += self.potion["effect"]["hp"]
        return result_hp

    def calculate_armour(self) -> int:
        result_armour = 0
        if self.armour:
            for armour_item in self.armour:
                result_armour += armour_item["protection"]
        if self.potion is not None:
            if "protection" in self.potion["effect"]:
                result_armour += self.potion["effect"]["protection"]
        return result_armour
