class Knight:
    """
    Class representing a knight and its attributes.

    Attributes:
        name (str): Knight's name
        base_power (int): Base power of the knight
        base_hp (int): Base health of the knight
        armour (list[dict]): List of armor pieces
        weapon (dict): Knight's weapon
        potion (Optional[dict]): Knight's potion (if any)
        power (int): Current power with equipment
        hp (int): Current health
        protection (int): Total protection from armor
    """

    def __init__(
            self, config: dict) -> None:
        self.name = config["name"]
        self.base_power = config["power"]
        self.base_hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0

    def prepare_for_battle(self) -> None:
        """Prepare the knight for battle: applying armor, weapon, and potion"""
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        """Calculate total protection from all armor pieces."""
        self.protection = sum(item["protection"] for item in self.armour)

    def _apply_weapon(self) -> None:
        """Add weapon's power to the knight's total power."""
        self.power += self.weapon["power"]

    def _apply_potion(self) -> None:
        """
        Apply potion effects, if available.
        May modify power, protection, and health of the knight.
        """
        if not self.potion:
            return

        effect = self.potion["effect"]
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        """
        Handle damage taken by the knight.

        Args:
            damage (int): Amount of damage to take
        """
        actual_damage = max(0, damage - self.protection)
        self.hp = max(0, self.hp - actual_damage)
