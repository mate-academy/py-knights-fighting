class Potion:

    possible_potion = {}

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
        self.__class__.possible_potion[name] = self

    def apply_potion(self, knight):
        for stat in ["power", "protection", "hp"]:
            if stat in self.effect:
                setattr(knight, stat,
                        getattr(knight, stat) + self.effect[stat])
