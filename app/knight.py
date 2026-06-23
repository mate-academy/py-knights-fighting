class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.armour = data.get("armour", [])
        self.weapon = data.get("weapon", {})
        self.potion = data.get("potion")
        self.protection = 0

    def apply_buffs(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon.get("power", 0)
        if self.potion:
            for stat, value in self.potion.get("effect", {}).items():
                setattr(self, stat, getattr(self, stat) + value)

    def take_damage(self, damage: int) -> None:
        self.hp = max(self.hp - damage, 0)

    def fight(self, opponent: "Knight") -> None:
        self.take_damage(opponent.power - self.protection)
        opponent.take_damage(self.power - opponent.protection)
