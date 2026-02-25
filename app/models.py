class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        self.power += config["weapon"]["power"]

        self.protection += sum(
            item["protection"] for item in config["armour"]
        )

        potion = config.get("potion")
        if potion:
            effects = potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def receive_damage(self, damage: int) -> None:
        actual_damage = damage - self.protection
        if actual_damage > 0:
            self.hp -= actual_damage

        if self.hp < 0:
            self.hp = 0
