class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect or {}

    def apply_effect(self, knight: dict) -> None:
        knight.hp += self.effect.get("hp", 0)
        knight.power += self.effect.get("power", 0)
        knight.protection += self.effect.get("protection", 0)
