from app.entities.behavior import EffectOnPower


class Weapon(EffectOnPower):
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
