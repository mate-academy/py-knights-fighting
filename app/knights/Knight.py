class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list | None = None,
                 weapon: dict | None = None,
                 potion: dict | None = None
                 ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.power = power
        self.hp = hp
        self.armour = armour if armour is not None else []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = 0
        if self.armour is not None:
            for item in self.armour:
                self.protection += item.get("protection", 0)
        if self.potion is not None and "protection" in self.potion.get("effect", {}):
            self.protection += self.potion["effect"]["protection"]
        self.protection = max(0, self.protection)

    def apply_weapon(self) -> None:
        self.power = self.base_power
        if self.weapon is not None:
            self.power += self.weapon.get("power", 0)
        if self.potion is not None and "power" in self.potion.get("effect", {}):
            self.power += self.potion["effect"]["power"]
        self.power = max(0, self.power)

    def apply_potion(self) -> None:
        self.hp = self.base_hp
        if self.potion is not None and "hp" in self.potion.get("effect", {}):
            self.hp += self.potion["effect"]["hp"]
        self.hp = max(0, self.hp)
