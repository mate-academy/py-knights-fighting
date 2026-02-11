class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.hp: int = config["hp"]
        self.power: int = config["power"]
        self.protection: int = 0

        # Internal configuration storage
        self._armour = config.get("armour", [])
        self._weapon = config.get("weapon", {})
        self._potion = config.get("potion")

        self._apply_gear()

    def _apply_gear(self) -> None:
        """Calculate effective stats before battle."""
        # Apply Armour
        self.protection += sum(item["protection"] for item in self._armour)

        # Apply Weapon
        self.power += self._weapon.get("power", 0)
        # Apply Potion
        if self._potion:
            effect = self._potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)

    def take_damage(self, opponent_power: int) -> None:
        """Calculate damage taken based on protection and floor at 0."""
        damage = opponent_power - self.protection
        if damage > 0:
            self.hp = max(0, self.hp - damage)
