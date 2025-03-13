class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config.get("potion", None)
        self.protection = 0

    def prepare(self) -> None:

        self.protection = sum(a["protection"] for a in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - max(0, damage - self.protection))
