class Potion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect = effect

        self._get_effects()

    def _get_effects(self) -> None:
        self.hp = self.effect.get("hp")
        self.power = self.effect.get("power")
        self.protection = self.effect.get("protection")