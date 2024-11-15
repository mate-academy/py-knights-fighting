from .equipment import Armour, Weapon, Potion


class Knight:
    """Represents a knight with stats and equipment."""

    def __init__(
        self, name: str, power: int, hp: int, armour: str, weapon: str,
        potion: str = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp

        # Validate armour structure
        if not isinstance(
            armour, list
        ) or not all(isinstance(a, dict) for a in armour):
            raise ValueError("Armour must be a list of dictionaries.")
        self.armour = [Armour(**a) for a in armour]

        # Validate weapon structure
        if not isinstance(weapon, dict):
            raise ValueError("Weapon must be a dictionary.")
        self.weapon = Weapon(**weapon)

        # Validate potion structure
        if potion and not isinstance(potion, dict):
            raise ValueError("Potion must be a dictionary.")
        self.potion = Potion(**potion) if potion else None

        self.protection = 0
        self.power = power

    def prepare_for_battle(self) -> None:
        """Apply all equipment and potion effects to prepare for battle."""
        self.protection = sum(a.protection for a in self.armour)
        self.power = self.base_power + self.weapon.power

        if self.potion:
            effect = self.potion.effect
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        """Reduce HP based on incoming damage."""
        self.hp -= max(0, damage)
        if self.hp < 0:
            self.hp = 0
