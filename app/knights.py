class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.base_hp: int = config["hp"]
        self.base_power: int = config["power"]
        self.armour: list[dict] = config.get("armour", [])
        self.weapon: dict = config["weapon"]
        self.potion: dict | None = config.get("potion")

        self.hp: int = self.calculate_hp()
        self.power: int = self.calculate_power()
        self.protection: int = self.calculate_protection()

    def calculate_hp(self) -> int:
        potion_hp = self.potion["effect"].get("hp", 0) if self.potion else 0
        return self.base_hp + potion_hp

    def calculate_power(self) -> int:
        weapon_power = self.weapon["power"]
        potion_power = self.potion["effect"].get("power", 0) \
            if self.potion else 0
        return self.base_power + weapon_power + potion_power

    def calculate_protection(self) -> int:
        armour_protection = sum(part["protection"]
                                for part in self.armour)
        potion_protection = self.potion["effect"].get("protection", 0) \
            if self.potion else 0
        return armour_protection + potion_protection
