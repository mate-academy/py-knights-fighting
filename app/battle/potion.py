class Potion:
    def __init__(self, name: str, hp_effect: int = 0, power_effect: int = 0) -> None:
        self.name = name
        self.hp_effect = hp_effect
        self.power_effect = power_effect

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__}('{self.name}', "
                f"HP Effect: {self.hp_effect}, Power Effect: {self.power_effect})>")
