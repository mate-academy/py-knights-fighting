from typing import Optional
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(
        self, name: str, power: int, hp: int,
        armour: Optional[list] = None, weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None
    ) -> None:
        self.name: str = name
        self.power: int = power
        self.hp: int = hp
        self.armour: list = armour if armour is not None else []
        self.weapon: Optional[Weapon] = weapon
        self.potion: Optional[Potion] = potion

    def apply_potion(self) -> None:
        """Applies the potion's effects to the knight's attributes."""
        if self.potion:
            self.hp += self.potion.hp_effect
            self.power += self.potion.power_effect

    def calculate_protection(self) -> int:
        """Calculates total protection from all pieces of armour."""
        return sum(item['protection'] for item in self.armour)

    def battle(self, opponent: 'Knight') -> None:
        """Simulates a battle between this knight and an opponent."""
        self.apply_potion()
        opponent.apply_potion()
        my_attack_power = self.power + (self.weapon.power if self.weapon else 0)
        opponent_attack_power = \
            opponent.power + (opponent.weapon.power if opponent.weapon else 0)
        my_protection = self.calculate_protection()
        opponent_protection = opponent.calculate_protection()

        # Calculate damage taken for both knights
        self.hp -= max(0, opponent_attack_power - my_protection)
        opponent.hp -= max(0, my_attack_power - opponent_protection)

        # Ensure HP does not drop below 0
        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)
