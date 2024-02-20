class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()
        self.apply_potion_effects()

    def calculate_protection(self) -> int:
        return sum(item["protection"] for item in self.armour)

    def apply_potion_effects(self) -> None:
        if self.potion:
            self.hp += self.potion["effect"].get("hp", 0)
            self.base_power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)

    @property
    def power(self) -> int:
        return self.base_power + self.weapon["power"]

    def receive_damage(self, damage: int) -> None:
        actual_damage = max(damage - self.protection, 0)
        self.hp = max(self.hp - actual_damage, 0)

    def __str__(self) -> str:
        return (f"{self.name} (HP: {self.hp}, Power: {self.power}, "
                f"Protection: {self.protection})")
