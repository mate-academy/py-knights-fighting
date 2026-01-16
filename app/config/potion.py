class Potion:
    def __init__(self, potion: dict = None) -> None:
        """
        Constructor for the Potion class

        This constructor initializes a Potion object with optional data
        If a potion dictionary is provided,
        it assigns the 'name' and 'effect' attributes from it
        If no potion dictionary is provided,
        'name' and 'effect' attributes are set to None
        """
        if potion is not None:
            self.name = potion["name"]
            self.effect = potion["effect"]
        else:
            self.name = None
            self.effect = None
