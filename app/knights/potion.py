class PotionEffect:
    def __init__(self, power: int = 0,
                 hp: int = 0,
                 protection: int = 0
                 ) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    def __repr__(self) -> str:
        effects = []
        if self.power is not None:
            effects.append(f"power={self.power}")
        if self.hp is not None:
            effects.append(f"hp={self.hp}")
        if self.protection is not None:
            effects.append(f"protection={self.protection}")
        return f"PotionEffect({", ".join(effects)})"


class Potion:
    def __init__(self, name: str, effect: PotionEffect) -> None:
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        return f"Potion(name='{self.name}', effect={self.effect})"
