class Potion:
    def __init__(self, potion: dict):
        self.name = None
        self.effect = {"power": 0, "hp": 0, "protection": 0}

        if potion:
            self.name = potion["name"]

            for kind in self.effect:
                if kind in potion["effect"]:
                    self.effect[kind] = potion["effect"][kind]
