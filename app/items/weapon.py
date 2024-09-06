class Weapon:
    """
    Represents a weapon used by the knight.
    Weapons add power to the knight, increasing
    their damage output during battles.

    Attributes:
        name (str): The name of the weapon.
        power (int): The power value that adds to the knight's base power.
    """
    def __init__(self, name: str, power: int) -> None:
        """
        Initializes the weapon with a name and power value.

        Args:
            name (str): The name of the weapon.
            power (int):
                The additional power the weapon provides to the knight.
        """
        self.name = name
        self.power = power
