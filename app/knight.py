class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")
        self.protection = 0

        self.apply_buffs()

    def apply_buffs(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, dmg: int) -> None:
        actual_damage = max(0, dmg - self.protection)
        self.hp = max(0, self.hp - actual_damage)
