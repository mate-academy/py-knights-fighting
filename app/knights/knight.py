class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.protection = 0

        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon", {})
        self.potion = config.get("potion")

    def prepare_for_battle(self) -> None:
        for part in self.armour:
            self.protection += part.get("protection", 0)

        if self.weapon:
            self.power += self.weapon.get("power", 0)

        if self.potion and "effect" in self.potion:
            effect = self.potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def fight(self, opponent: "Knight") -> None:
        damage_taken = max(0, opponent.power - self.protection)
        self.hp = max(0, self.hp - damage_taken)
