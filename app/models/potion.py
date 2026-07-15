class Potion:
    def __init__(self, name: str, effect: dict | None = None) -> None:
        """
        Initializes a potion with its name and statistical modifiers.
        """
        self.name = name
        self.effect = effect or {}

    def get_modifier(self, stat_name: str) -> int:
        """
        Returns the modifier value for a specific stat (e.g., 'hp', 'power').
        Returns 0 if the stat is not affected by this potion.
        """
        return self.effect.get(stat_name, 0)
