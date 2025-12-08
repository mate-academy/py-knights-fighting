class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armor(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if "power" in self.potion["effect"]:
            self.power += self.potion["effect"]["power"]

        if "protection" in self.potion["effect"]:
            self.protection += self.potion["effect"]["protection"]

        if "hp" in self.potion["effect"]:
            self.hp += self.potion["effect"]["hp"]

    def prepare_knight_to_fight(self) -> dict:
        self.apply_armor()
        self.apply_weapon()
        if self.potion is not None:
            self.apply_potion()
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection,
        }
