class Knight:
    def __init__(
            self, name: str, power: int, hp: int, armour: int,
            weapon: int, potion: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.apply_effects()

    def apply_effects(self) -> None:
        for armor_part in self.armour:
            self.protection += armor_part["protection"]
        self.power += self.weapon["power"]
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def get_damage(self, opponent_protection: dict) -> None:
        return max(0, self.power - opponent_protection)
