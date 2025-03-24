from app.PotionEffect import PotionEffect


class Potion:
    def __init__(self, name: str, effect: PotionEffect) -> None:
        self.__name: str = name
        self.__effect: PotionEffect = effect

    @property
    def name(self) -> str:
        return self.__name

    @property
    def effect(self) -> PotionEffect:
        return self.__effect

    def __repr__(self) -> str:
        return f"Potion(name='{self.name}', effect={self.effect})"
