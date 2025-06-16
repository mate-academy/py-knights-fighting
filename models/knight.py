class Knight:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", None)
        self.potion = config.get("potion", None)

        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.protection = sum(a.get("protection", 0) for a in self.armour)

        if self.weapon:
            self.power += self.weapon.get("power", 0)

        if self.potion and self.potion.get("effect"):
            effects = self.potion["effect"]
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def receive_damage(self, attack_power: int):
        damage = max(attack_power - self.protection, 0)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
