class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict[str, int]] | None = None,
                 weapon: dict[str, int | str] | None = None,
                 potion: dict[str, dict[str, int] | str] | None = None
                 ) -> None :
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        if armour is None:
            self.armour = []
        else:
            self.armour = [
                item for item in armour
                if isinstance(item, dict)
                and "part" in item
                and "protection" in item
            ]

        if weapon is None:
            self.weapon = {
                "name": "No Weapon",
                "power": 0
            }
        elif (isinstance(weapon, dict)
              and "name" in weapon
              and "power" in weapon):
            self.weapon = weapon
        else:
            raise ValueError("Incorrect weapon format")

        if potion is None:
            self.potion = None
        elif (
            isinstance(potion, dict)
            and "name" in potion
            and "effect" in potion
            and isinstance(potion["effect"], dict)
        ):
            self.potion = potion
        else:
            raise ValueError("Incorrect potion format")

        self.add_armour_protection()
        self.add_weapon_power()
        self.add_potion()

    def add_armour_protection(self) -> None:
        for item in self.armour :
            self.protection = self.protection + item["protection"]

    def add_weapon_power(self) -> None:
        self.power += self.weapon.get("power", 0)

    def add_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
