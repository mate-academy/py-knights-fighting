from app.models.potion import Potion
from app.models.weapon import Weapon
from app.models.armour import Armour


class Knight:
    def __init__(
            self,
            name: str,
            base_power: int,
            base_hp: int,
            armour: Armour,
            weapon: Weapon,
            potion: Potion | None
    ) -> None:
        """
        Initializes the knight object.
        Accepts name, power and hp.
        """
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.hp = base_hp + self._get_potion_boost("hp")
        self.power = (
            base_power
            + self.weapon.power
            + self._get_potion_boost("power")
        )
        self.protection = (
            self.armour.calculate_total_protection()
            + self._get_potion_boost("protection")
        )

    def _get_potion_boost(self, stat_name: str) -> int:
        """Helper method to safely pull modifiers if a potion is equipped."""
        if self.potion is None:
            return 0
        return self.potion.get_modifier(stat_name)
