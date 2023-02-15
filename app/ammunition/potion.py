class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self._name = name
        self._effect = effect

    @property
    def name(self) -> str:
        return self._name

    @property
    def effect(self) -> dict:
        return self._effect
