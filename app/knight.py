

class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict | None,
                 protection: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self) -> None:
        # apply armour
        self.protection = 0
        for arm in self.armour:
            self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        # apply weapon
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare_to_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
