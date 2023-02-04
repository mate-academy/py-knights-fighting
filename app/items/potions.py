from app.buffs.PotionEffects import PotionEffects


class Potion:
    def __init__(
            self,
            name: str,
            effect: PotionEffects,
    ) -> None:
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Potion: {self.name}"
