class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.hp = data["hp"]
        self.power = data["power"]
        self.protection = 0

        self._apply_armour(data["armour"])
        self._apply_weapon(data["weapon"])
        self._apply_potion(data["potion"])

    def _apply_armour(self, armour: list) -> None:
        self.protection = sum(
            part["protection"]
            for part in armour
        )

    def _apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _apply_potion(self, potion: dict | None) -> None:
        if potion is None:
            return

        for stat, value in potion["effect"].items():
            setattr(
                self,
                stat,
                getattr(self, stat) + value
            )

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        self.hp = max(0, self.hp - damage)
