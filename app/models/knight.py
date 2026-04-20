class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        self.apply_equipment(config)

    def apply_equipment(self, config: dict) -> None:
        self.power += config["weapon"]["power"]
        for armor_part in config["armour"]:
            self.protection += armor_part["protection"]

        potion = config.get("potion")
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        actual_damage = opponent_power - self.protection
        if actual_damage > 0:
            self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0

    @staticmethod
    def fight(knight1: "Knight", knight2: "Knight") -> None:
        k1_initial_power = knight1.power
        k2_initial_power = knight2.power

        knight1.take_damage(k2_initial_power)
        knight2.take_damage(k1_initial_power)
