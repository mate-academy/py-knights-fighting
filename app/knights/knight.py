from typing import List, Optional
from app.knights.equipment import Armour, Weapon, Potion


class Knight:
    """
    Encapsulates the state and behavior of a single knight.

    Attributes:
        name (str): The knight's display name.
        base_power (int): The knight's base attack power (before adding weapon/potion).
        current_hp (int): The knight's current hit points.
        armour (List[Armour]): A list of Armour objects the knight is wearing.
        weapon (Optional[Weapon]): The Weapon object the knight wields, or None if unarmed.
        potion (Optional[Potion]): The Potion object the knight carries, or None if no potion.
        power (int): The knight's final attack power after applying weapon and potion effects.
        protection (int): The knight's total protection value after summing armour and potion effects.
    """

    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: Optional[List[Armour]] = None,
        weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None,
    ):
        self.name = name
        self.base_power = base_power
        self.current_hp = base_hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        # Compute final values for power and protection (and apply potion HP effect).
        self._apply_equipment_and_potions()

    def _apply_equipment_and_potions(self):
        """
        Calculates total protection from all armour pieces, adds weapon power to base_power,
        and applies any potion effects (modifying power, protection, and/or HP).
        """
        # Sum protection from all armour pieces.
        self.protection = sum(piece.protection for piece in self.armour)

        # Add weapon power if a weapon is equipped.
        self.power = self.base_power + (self.weapon.power if self.weapon else 0)

        # Apply potion effects if present.
        if self.potion:
            effects = self.potion.effect
            if "power" in effects:
                self.power += effects["power"]
            if "protection" in effects:
                self.protection += effects["protection"]
            if "hp" in effects:
                self.current_hp += effects["hp"]

    def receive_damage(self, damage_amount: int):
        """
        Reduces the knight's current HP by (damage_amount - protection).
        If net damage <= 0, HP remains unchanged. HP is floored at 0.
        Args:
            damage_amount (int): The raw incoming attack power from an opponent.
        """
        net_damage = damage_amount - self.protection
        if net_damage > 0:
            self.current_hp -= net_damage
        if self.current_hp < 0:
            self.current_hp = 0

    def is_alive(self) -> bool:
        """
        Returns True if the knight's current HP is greater than 0.
        """
        return self.current_hp > 0

    def __repr__(self):
        return (
            f"<Knight {self.name}: HP={self.current_hp}, "
            f"Power={self.power}, Protection={self.protection}>"
        )
