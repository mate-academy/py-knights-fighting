class Knight:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.base_power = config["power"]
        self.hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")
        self.power = self.base_power
        self.protection = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self):
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self):
        self.power += self.weapon["power"]

    def apply_potion(self):
        if not self.potion:
            return
        effect = self.potion["effect"]
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
