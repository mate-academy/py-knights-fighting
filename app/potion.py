class Potion:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


berserk = Potion("Berserk", power=+15, hp=-5, protection=+10)
blessing = Potion("Blessing", power=+5, hp=+10, protection=0)
