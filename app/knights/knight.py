class Knight:
    def __init__(
            self, name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.prtection = 0

        if self.armour:
            for armour_piece in self.armour:
                self.prtection += armour_piece["protection"]

        if self.weapon:
            self.power += self.weapon["power"]

        if self.potion:
            if self.potion["effect"].get("power"):
                self.power += self.potion["effect"]["power"]
            if self.potion["effect"].get("hp"):
                self.hp += self.potion["effect"]["hp"]
            if self.potion["effect"].get("protection"):
                self.prtection += self.potion["effect"]["protection"]
