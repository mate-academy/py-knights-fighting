class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"] + config["weapon"]["power"]
        self.protection = sum(part["protection"] for part in config["armour"])

        potion = config["potion"]
        if potion is not None:
            effect = potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, enemy_power: int) -> None:
        self.hp -= enemy_power - self.protection
        if self.hp <= 0:
            self.hp = 0
