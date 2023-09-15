class Potion:
    def __init__(self, name, effect) -> None:
        self.name = name
        self.effect = effect

    def apply(self, knight) -> None:
        knight.hp += self.effect.get("hp", 0)
        knight.power += self.effect.get("power", 0)
        knight.protection += self.effect.get("protection", 0)
