class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict[str | int]],
            weapon: dict[str | int],
            potion: bool | dict,
    ) -> None:
        self.name = name
        self.power = self.get_power(power, weapon)
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.protection = self.get_protection()
        self.potion = potion
        self.calculate_potion_effect()

    def calculate_potion_effect(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    @staticmethod
    def get_power(power: int, weapon: dict[str | int], ) -> int:
        return power + weapon["power"]

    def get_protection(self) -> int:
        return sum(a["protection"] for a in self.armour)
