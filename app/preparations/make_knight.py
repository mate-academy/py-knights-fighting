class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def prepare_knight(self) -> dict:
        return {
            "name": self.name,
            "strength": (
                self.power
                + self.weapon["power"]
                + self.stat_boost("power")
            ),
            "hp": self.hp + self.stat_boost("hp"),
            "protection": sum([part["protection"] for part in self.armour])
                          + self.stat_boost("protection"),
        }

    def stat_boost(self, stat: str) -> int:
        if self.potion is None:
            return 0

        return self.potion["effect"].get(stat, 0)
