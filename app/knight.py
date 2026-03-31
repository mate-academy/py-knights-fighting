class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.hp = knight_data["hp"]
        self.power = knight_data["power"]
        self.protection = 0

        self._apply_armour(knight_data.get("armour", []))
        self._apply_weapon(knight_data.get("weapon", {}))
        self._apply_potion(knight_data.get("potion"))

    def _apply_armour(self, armour_list: list) -> None:
        for part in armour_list:
            self.protection += part.get("protection", 0)

    def _apply_weapon(self, weapon: dict) -> None:
        if weapon:
            self.power += weapon.get("power", 0)

    def _apply_potion(self, potion: dict | None) -> None:
        if potion and "effect" in potion:
            effect = potion["effect"]
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
