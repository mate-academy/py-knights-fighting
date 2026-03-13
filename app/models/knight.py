class Knight:
    def __init__(self, stats: dict) -> None:
        self.name: str = stats["name"]
        self.hp: int = stats["hp"]
        self.power: int = stats["power"]
        self.protection: int = 0
        for item in stats.get("armour", []):
            self.protection += item["protection"]
        self.power += stats["weapon"]["power"]
        potion = stats.get("potion")
        if potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
