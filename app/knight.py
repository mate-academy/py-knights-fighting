class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.protection = 0
        self.potion = potion
        self.is_prepared = False

    def battle_preparation(self) -> None:
        if self.is_prepared:
            return
        protection = 0
        for armour_item in self.armour:
            protection += armour_item["protection"]
        self.protection = protection

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
        self.is_prepared = True
