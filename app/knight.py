class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: dict, potion: dict = None):
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_power(self):
        power = self.base_power + self.weapon["power"]
        if self.potion and "effect" in self.potion and "power" in self.potion["effect"]:
            power += self.potion["effect"]["power"]
        return power

    def get_hp(self):
        hp = self.base_hp
        if self.potion and "effect" in self.potion and "hp" in self.potion["effect"]:
            hp += self.potion["effect"]["hp"]
        return hp

    def get_protection(self):
        protection = sum([equip["protection"] for equip in self.armour])
        if self.potion and "effect" in self.potion and "protection" in self.potion["effect"]:
            protection += self.potion["effect"]["protection"]
        return protection
