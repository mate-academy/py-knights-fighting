class Knight:
    def __init__(self, config: str) -> None:
        self.name = config["name"]
        self.base_power = config["power"]
        self.base_hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", {})
        self.potion = config.get("potion", None)
        self.protection = 0
        self.power = 0
        self.hp = 0
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.protection = sum(item["protection"] for item in self.armour)
        self.power = self.base_power + self.weapon.get("power", 0)
        self.hp = self.base_hp

        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
