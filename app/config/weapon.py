class Weapon:
    def __init__(self, weapon: dict) -> None:
        """
        Constructor for the Weapon class

        This constructor initializes a Weapon object
        using the provided dictionary
        It assigns the 'name' and 'power' attributes
        from the dictionary
        """
        self.name = weapon["name"]
        self.power = weapon["power"]
