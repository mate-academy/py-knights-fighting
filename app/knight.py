class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.base_hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]
        self.hp = 0
        self.power = 0
        self.protection = 0
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0
        self.power += self.weapon["power"]

        for part in self.armour:
            self.protection += part["protection"]

        if self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        actual_damage = opponent_power - self.protection
        if actual_damage > 0:
            self.hp -= actual_damage

        if self.hp < 0:
            self.hp = 0
