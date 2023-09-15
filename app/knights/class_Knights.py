class KnightInstances:
    instances = {}

    def __init__(
            self,
            knight_name,
            knight_data
    ) -> None:
        self.name = knight_data.get("name")
        self.power = knight_data.get("power", 0)
        self.hp = knight_data.get("hp", 0)
        self.armour = knight_data.get("armour", [])
        self.weapon = knight_data.get("weapon", {})
        self.potion = knight_data.get("potion", None)
        self.protection = 0
        KnightInstances.instances[knight_name] = self

    def apply_armour(self) -> None:
        for current_armour in self.armour:
            self.protection += current_armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def vs(self, other) -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0

    def enter_method(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion_if_exist()
