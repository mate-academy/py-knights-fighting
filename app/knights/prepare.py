class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, armour: list, weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.armor = armour
        self.potion = potion
        self.protection = 0

    def __str__(self) -> str:
        return (f"{self.name} has hp {self.hp}, "
                f"power {self.power}, protection {self.protection}")

    def apply_armour(self) -> None:
        protection = 0
        for piece in self.armor:
            protection += piece["protection"]
        self.protection = protection

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
