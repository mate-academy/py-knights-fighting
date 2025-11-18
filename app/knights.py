class Knight:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.hp = config["hp"]
        self.base_power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", {"power": 0})
        self.potion = config.get("potion")
        self.power = self.base_power
        self.protection = 0

    def prepare_for_battle(self):
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon.get("power", 0)

        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def fight(self, opponent: "Knight"):
        damage_to_self = max(opponent.power - self.protection, 0)
        damage_to_opponent = max(self.power - opponent.protection, 0)

        self.hp = max(self.hp - damage_to_self, 0)
        opponent.hp = max(opponent.hp - damage_to_opponent, 0)
