class Knight:

    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.hp = config["hp"]
        self.power = config["power"]
        self.armour = config.get("armour", [])
        self.weapon = config["weapon"]
        self.potion = config.get("potion")
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if not self.potion:
            return
        effects = self.potion.get("effect", {})
        for stat, value in effects.items():
            if hasattr(self, stat):
                setattr(self, stat, getattr(self, stat) + value)
            else:
                setattr(self, stat, value)

    def duel(self, opponent: "Knight") -> None:
        self_damage = max(0, opponent.power - self.protection)
        opponent_damage = max(0, self.power - opponent.protection)

        self.hp -= self_damage
        opponent.hp -= opponent_damage

        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)

    def __repr__(self) -> str:
        return (f"<Knight {self.name}: "
                f"HP={self.hp}, Power={self.power}, "
                f"Prot={self.protection}>")
