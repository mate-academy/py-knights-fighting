class Knights:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armours: list,
            weapon: dict,
            potion: dict | None,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def preparing_knight_battle(self) -> None:
        for armour in self.armours:
            self.protection += armour["protection"]
        self.power += self.weapon["power"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def check_if_someone_fell_in_battle(self) -> None:
        if self.hp <= 0:
            self.hp = 0
