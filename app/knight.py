class Knight:
    def __init__(
        self,
        knights_config: dict
    ) -> None:
        self.name = knights_config["name"]
        self.base_power = knights_config["power"]
        self.hp = knights_config["hp"]
        self.armour = knights_config["armour"]
        self.weapon = knights_config["weapon"]
        self.potion = knights_config["potion"]
        self.power = self.base_power
        self.protection = 0

    def apply_equipment(self) -> None:
        if self.armour:
            self.protection = sum(item["protection"] for item in self.armour)

        if self.weapon:
            self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def receive_damage(self, attack_power: int) -> None:
        damage = max(0, attack_power - self.protection)
        self.hp = max(0, self.hp - damage)
