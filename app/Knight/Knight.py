class Knight:
    def __init__(
            self,
            knight: dict,
            protection: int = 0,
    ) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = protection

    def prepare_to_battle(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def fight(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection

        if self.hp < 0:
            self.hp = 0
