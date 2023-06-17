class Potion:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")
        effect = stats.get("effect")
        if effect is not None:

            if effect.get("hp") is not None:
                self.hp = effect.get("hp")
            else:
                self.hp = 0

            if effect.get("power") is not None:
                self.power = effect.get("power")
            else:
                self.power = 0

            if effect.get("protection") is not None:
                self.protection = effect.get("protection")
            else:
                self.protection = 0
