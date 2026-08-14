class Potion:
    """Represents consumable potion that will provide Knight
        with extra stats when consumed.
    """
    def __init__(self, name: str, effect: dict) -> None:
        """INIT"""
        self.name = name
        self.effect = effect
