class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]
        self.base_hp: int = config["hp"]
        self.base_power: int = config["power"]
        self.armour: list = config.get("armour", [])
        self.weapon: dict = config.get("weapon", {})
        self.potion: dict = config.get("potion", None)
        self.hp: int = 0
        self.power: int = 0
        self.protection: int = 0

        self._prepare_for_battle()

    def _prepare_for_battle(self) -> None:
        # Applies armour, weapons, and potion effects before battle.
        self.hp = self.base_hp
        self.power = self.base_power + self.weapon.get("power", 0)
        self.protection = sum(part["protection"] for part in self.armour)

        if self.potion:
            effects = self.potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def receive_damage(self, opponent_power: int) -> None:
        # Calculates received damage based on
        # opponent's power and self-protection.
        effective_damage = opponent_power - self.protection
        if effective_damage > 0:
            self.hp -= effective_damage

        # Ensure HP does not drop below 0
        if self.hp < 0:
            self.hp = 0

    def fight(self, opponent: "Knight") -> None:
        # Simulates a simultaneous battle between two knights.
        self_power = self.power
        opponent_power = opponent.power

        self.receive_damage(opponent_power)
        opponent.receive_damage(self_power)
