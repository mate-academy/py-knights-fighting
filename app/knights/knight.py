class Knight:

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.base_power = data["power"]
        self.armour = data.get("armour", [])
        self.weapon = data["weapon"]
        self.potion = data.get("potion")
        self.protection = 0
        self.power = self.base_power
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            effects = self.potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def fight(self, opponent: "Knight") -> None:
        self.hp -= max(0, opponent.power - self.protection)
        opponent.hp -= max(0, self.power - opponent.protection)

        # No negative HP
        self.hp = max(self.hp, 0)
        opponent.hp = max(opponent.hp, 0)
