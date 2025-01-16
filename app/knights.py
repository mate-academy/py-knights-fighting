class Knight:

    def __init__(self, name: str, stats: dict):
        self.name = name
        self.base_hp = stats["hp"]
        self.base_power = stats["power"]
        self.armour = stats.get("armour", [])
        self.weapon = stats.get("weapon", {})
        self.potion = stats.get("potion", {})

        # Применение модификаций
        self.hp = self.base_hp + self.potion_effect("hp", 0)
        self.power = (
            self.base_power
            + self.weapon.get("power", 0)
            + self.potion_effect("power", 0)
        )
        self.protection = (
            sum(armour.get("protection", 0) for armour in self.armour)
            + self.potion_effect("protection", 0)
        )

    def potion_effect(self, key: str, default: int) -> int:
        return self.potion.get("effect", {}).get(key, default)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def __repr__(self):
        return f"Knight(name={self.name}, hp={self.hp}, power={self.power}, protection={self.protection})"
