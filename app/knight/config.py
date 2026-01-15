class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = None,
                 weapon: dict = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

        if self.weapon:
            self.power += self.weapon["power"]

        if self.potion:
            if self.potion["effect"].get("power"):
                self.power += self.potion["effect"]["power"]

            if self.potion["effect"].get("protection"):
                self.protection += self.potion["effect"]["protection"]

            if self.potion["effect"].get("hp"):
                self.hp += self.potion["effect"]["hp"]
