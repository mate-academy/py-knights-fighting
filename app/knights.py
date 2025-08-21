class Knight:
    def __init__(self, config: dict):
        self.name = config.get("name", "Unknown Knight")
        self.base_hp = config.get("hp", 0)
        self.base_power = config.get("power", 0)
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", {"power": 0})
        self.potion = config.get("potion")

        self.hp = self.calculate_hp()
        self.power = self.calculate_power()
        self.protection = self.calculate_protection()

    def calculate_hp(self):
        effect = self.potion.get("effect", {}) if self.potion else {}
        return self.base_hp + effect.get("hp", 0)

    def calculate_power(self):
        effect = self.potion.get("effect", {}) if self.potion else {}
        return self.base_power + self.weapon.get("power", 0) + effect.get("power", 0)

    def calculate_protection(self):
        base = sum(part.get("protection", 0) for part in self.armour)
        effect = self.potion.get("effect", {}) if self.potion else {}
        return base + effect.get("protection", 0)
