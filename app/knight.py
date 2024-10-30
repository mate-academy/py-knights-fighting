class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_power = config["power"]
        self.hp = config["hp"]
        self.armor = config.get("armour", [])
        self.weapon = config.get("weapon", {})
        self.potion = config.get("potion", None)
        self.protection = 0

        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        self.protection = sum(part["protection"] for part in self.armor)

    def apply_weapon(self) -> None:
        self.base_power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.base_power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    @property
    def total_power(self) -> int | float:
        return self.base_power

    @property
    def total_protection(self) -> int | float:
        return self.protection

    def adjust_hp(self, opponent_power: int | float) -> None:
        damage = max(0, opponent_power - self.total_protection)
        self.hp = max(0, self.hp - damage)
