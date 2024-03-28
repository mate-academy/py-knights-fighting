class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict,
    ) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = sum(item["protection"] for item in armour)
        # Apply potion effects if not None
        if potion:
            self.hp += potion["effect"].get("hp", 0)
            self.power += potion["effect"].get("power", 0)
            self.protection += potion["effect"].get("protection", 0)

    def calculate_damage(self, opponent: "Knight") -> int:
        # Calculate initial damage
        initial_damage = self.power - opponent.protection
        return max(1, initial_damage) if initial_damage > 0 else 0
