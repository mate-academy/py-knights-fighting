from app.components.effect import Effect


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = Effect(effect["hp"], effect["power"],
                             effect.get("protection"))

    def __repr__(self) -> str:
        return str(self.__dict__)
