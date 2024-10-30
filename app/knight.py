class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion", None)
        self.protection = self.calculate_protection()
        self.apply_weapon()
        self.apply_potion()

    def calculate_protection(self) -> int | float:
        base_protection = sum(part["protection"] for part in self.armour)
        return base_protection

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int | float) -> None:
        self.hp -= opponent_power - self.protection

    def is_defeated(self) -> bool:
        return self.hp <= 0
