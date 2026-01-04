class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.stats = self.calculate_stats()

    def calculate_stats(self) -> dict:
        protection = sum(item["protection"] for item in self.armour)
        weapon_power = self.weapon["power"]
        potion_effect = (
            self.potion["effect"]
            if self.potion
            else {"hp": 0, "power": 0, "protection": 0}
        )

        return {
            "hp": self.hp + potion_effect.get("hp", 0),
            "power": (
                self.base_power + weapon_power + potion_effect.get("power", 0)
            ),
            "protection": protection + potion_effect.get("protection", 0)
        }

    def take_damage(self, opponent_power: int) -> None:
        damage = max(opponent_power - self.stats["protection"], 0)
        self.stats["hp"] = max(self.stats["hp"] - damage, 0)
