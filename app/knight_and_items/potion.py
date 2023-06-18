class Potion:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")

        self.hp = 0
        self.power = 0
        self.protection = 0

        self.apply_effects(stats.get("effect"))

    def apply_effects(self, effect: dict) -> None:
        if effect is not None:

            if effect.get("hp") is not None:
                self.hp = effect.get("hp")

            if effect.get("power") is not None:
                self.power = effect.get("power")

            if effect.get("protection") is not None:
                self.protection = effect.get("protection")
