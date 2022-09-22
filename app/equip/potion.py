class Potion:
    def __init__(self, potion: dict):
        self.potion = potion

    def get_potion(self, hero) -> None:
        if self.potion is not None:
            for stats in ["hp", "protection", "power"]:
                if stats in self.potion["effect"]:
                    hero.__dict__[stats] += self.potion["effect"][stats]
