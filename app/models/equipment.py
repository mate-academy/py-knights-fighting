class Equipment:
    def __init__(
        self,
        name: str,
        power: int = 0,
        hp: int = 0,
        prot: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = prot


class Potion(Equipment):
    def __init__(self, name: str, effect: dict) -> None:
        super().__init__(
            name,
            power=effect.get("power", 0),
            hp=effect.get("hp", 0),
            prot=effect.get("protection", 0)
        )
