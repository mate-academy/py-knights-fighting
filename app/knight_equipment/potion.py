class Potion:
    def __init__(self, name: str, effect: dict = None) -> None:
        self.name = name
        self.effect = effect
        self.effect_hp = 0
        self.effect_power = 0
        self.effect_protection = 0

    def drink_potion(self) -> dict:
        if self.effect:
            if self.effect.get("hp"):
                self.effect_hp = self.effect.get("hp")
            if self.effect.get("power"):
                self.effect_power = self.effect.get("power")
            if self.effect.get("protection"):
                self.effect_protection = self.effect.get("protection")
        return {"effect_hp": self.effect_hp,
                "effect_power": self.effect_power,
                "effect_protection": self.effect_protection}
