from typing import Tuple

class Knight:
    def __init__(self, name: str, power: int, hp: int, weapon=None, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.potion = potion

    def get_protection(self) -> int:
        # Placeholder method to represent getting total protection.
        # This should include logic to sum up protection from armor and effects.
        return 0

def calculate_damage(attacker_power: int, defender_protection: int) -> int:
    """Calculate damage based on attacker's power and defender's protection."""
    damage = attacker_power - defender_protection
    return max(damage, 0)  # Prevent negative damage

def battle(knight1: Knight, knight2: Knight) -> Tuple[int, int]:
    """Simulate a battle between two knights, returning their final HPs."""
    # Apply potion effects
    if knight1.potion:
        knight1.hp += knight1.potion.hp_effect
        knight1.power += knight1.potion.power_effect
    
    if knight2.potion:
        knight2.hp += knight2.potion.hp_effect
        knight2.power += knight2.potion.power_effect

    # Calculate damage to each knight
    damage_to_knight1 = calculate_damage(
        knight2.power + (knight2.weapon.power if knight2.weapon else 0),
        knight1.get_protection()
    )
    damage_to_knight2 = calculate_damage(
        knight1.power + (knight1.weapon.power if knight1.weapon else 0),
        knight2.get_protection()
    )

    # Adjust HP based on damage
    knight1.hp = max(knight1.hp - damage_to_knight1, 0)
    knight2.hp = max(knight2.hp - damage_to_knight2, 0)

    return knight1.hp, knight2.hp
