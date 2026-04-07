class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.power: int = config["power"]
        self.protection: int = 0
        self.apply_equipment(config)

    def apply_equipment(self, config: dict) -> None:
        for item in config.get("armour", []):
            self.protection += item["protection"]

        weapon = config.get("weapon")
        if weapon:
            self.power += weapon["power"]

        potion = config.get("potion")
        if potion:
            effect = potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def get_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0
