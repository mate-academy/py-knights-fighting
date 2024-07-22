class Knight:
    def __init__(self, name: str,
                 power: int, hp: int,
                 armour: list, weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.protection = 0
        for armour_piece in self.armour:
            self.protection += armour_piece.get("protection", 0)

        self.power = self.base_power + self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def take_damage(self, damage: int) -> None:
        self.hp -= damage - self.protection
        if self.hp < 0:
            self.hp = 0
