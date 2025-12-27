class Knight:
    """Represents a knight with their equipment and stats."""

    def __init__(self, config: dict) -> None:
        """Initialize a knight from configuration dictionary."""
        self.name = config["name"]
        self.base_power = config["power"]
        self.base_hp = config["hp"]
        self.armour = config.get("armour", [])
        self.weapon = config.get("weapon")
        self.potion = config.get("potion")

        # Calculated stats after applying equipment
        self.power = 0
        self.hp = 0
        self.protection = 0

    def prepare_for_battle(self) -> None:
        """Apply all equipment effects before battle."""
        # Start with base stats
        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0

        # Apply armour
        self._apply_armour()

        # Apply weapon
        self._apply_weapon()

        # Apply potion if exists
        self._apply_potion()

    def _apply_armour(self) -> None:
        """Calculate total protection from all armour pieces."""
        for armour_piece in self.armour:
            self.protection += armour_piece.get("protection", 0)

    def _apply_weapon(self) -> None:
        """Add weapon power to knight's power."""
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def _apply_potion(self) -> None:
        """Apply potion effects to knight's stats."""
        if self.potion is None:
            return

        effect = self.potion.get("effect", {})

        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, opponent_power: int) -> None:
        """Reduce HP based on opponent's power and own protection."""
        damage = opponent_power - self.protection
        self.hp -= damage

        # Knight cannot have negative HP
        if self.hp < 0:
            self.hp = 0

    def __repr__(self) -> str:
        return (f"Knight({self.name}, HP: {self.hp}, "
                f"Power: {self.power}, Protection: {self.protection})")
