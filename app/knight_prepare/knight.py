class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list = None,
            potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def equip_knight(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]

            if "power" in effect:
                self.power += effect["power"]

            if "protection" in effect:
                self.protection += effect["protection"]

            if "hp" in effect:
                self.hp += effect["hp"]
