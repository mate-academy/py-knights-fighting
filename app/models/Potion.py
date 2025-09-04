class Potion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect = effect

    @classmethod
    def from_dict(cls, data: dict):
        if not data:
            return None
        name = data.get("name", )
        effect = cls.Effect.from_dict(data.get("effect", {}))
        return cls(name, effect)

    def __str__(self):
        return f"Potion {self.name}: {self.effect}"

    class Effect:
        def __init__(self, power: int = 0, protection: int = 0, hp: int = 0):
            self.power = power
            self.protection = protection
            self.hp = hp

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                power=data.get("power", 0),
                protection=data.get("protection", 0),
                hp=data.get("hp", 0)
            )

        def __str__(self):
            return f"Effect(power={self.power}, protection={self.protection}, hp={self.hp})"