class Potion:
    """
    Represents a potion that affects the knight's stats.
    Potions can increase or decrease
    the knight's health points (hp), power, and protection.

    Attributes:
        name (str): The name of the potion.
        effect (dict[str, int]):
            The effect of the potion,
            which can modify hp, power, and protection.
    """

    def __init__(self, name: str, effect: dict[str, int]) -> None:
        """
        Initializes the potion with a name and a set of effects
        on the knight's stats.

        Args:
            name (str): The name of the potion.
            effect (dict[str, int]):
                A dictionary representing how the potion affects
                knight's hp, power, and protection.
        """
        self.name = name
        self.effect = effect
