class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_power = config["power"]
        self.hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")

        self.power = self.base_power
        self.protection = 0

        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def receive_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
