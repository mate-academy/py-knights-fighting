class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | list[dict],
            weapon: dict,
            potion: None | dict
    ) -> None:
        self.protection = None
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = 0
        for armour in self.armour:
            self.protection += armour["protection"]
        # print(self.protection)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)
        # print(f"{self.name} weapon power is {self.power}")

    def apply_potion(self) -> None:
        if self.potion is not None:
            effects = self.potion.get("effect", {})

            if "power" in effects:
                self.power += effects["power"]

            if "protection" in effects:
                self.protection += effects["protection"]

            if "hp" in effects:
                self.hp += effects["hp"]
        # print(f"{self.name} has power - {self.power}, protection - {self.protection}, hp - {self.hp}")
