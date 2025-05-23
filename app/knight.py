class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")

        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, enemy_power: int) -> None:
        damage = max(enemy_power - self.protection, 0)
        self.hp = max(self.hp - damage, 0)
