class Knight:
    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.hp = stats["hp"]
        self.power = stats["power"] + stats["weapon"]["power"]
        self.protection = sum(
            part["protection"] for part in stats["armour"]
        )

        if stats["potion"] is not None:
            self.apply_potion(stats["potion"]["effect"])

    def apply_potion(self, effects: dict) -> None:
        for stat, change in effects.items():
            current_value = getattr(self, stat)
            setattr(self, stat, current_value + change)

    def receive_hit(self, opponent: "Knight") -> None:
        damage = opponent.power - self.protection
        self.hp = max(0, self.hp - damage)
