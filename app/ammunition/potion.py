class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply_effect(self, hp: int, power: int, protection: int) -> tuple:
        new_hp = hp + self.effect.get("hp", 0)
        new_power = power + self.effect.get("power", 0)
        new_protection = protection + self.effect.get("protection", 0)
        return new_hp, new_power, new_protection
