class Potion:
    def __init__(self,
                 p_name: str = "Unknown",
                 effect=None
                 ) -> None:

        if effect is None:
            effect = {}
        self.name = p_name
        self.effect = effect
