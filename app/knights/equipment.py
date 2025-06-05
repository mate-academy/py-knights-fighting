from dataclasses import dataclass
from typing import Dict


@dataclass
class Armour:
    """
    Represents a single piece of armour (helmet, breastplate, boots, etc.).
    Attributes:
        part (str): The body part that this armour covers.
        protection (int): The protection value provided by this armour.
    """
    part: str
    protection: int


@dataclass
class Weapon:
    """
    Represents a weapon for a knight.
    Attributes:
        name (str): The name of the weapon.
        power (int): The attack power provided by this weapon.
    """
    name: str
    power: int


@dataclass
class Potion:
    """
    Represents a potion and its effects.
    Attributes:
        name (str): The name of the potion.
        effect (Dict[str, int]): A dictionary of effects, possibly containing keys 'power', 'protection', 'hp',
                                 each mapping to an integer (positive or negative).
    """
    name: str
    effect: Dict[str, int]
