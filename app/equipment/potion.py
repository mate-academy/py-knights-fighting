class Potion:
    potions_arr = {}

    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            protection: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

        if self.name not in Potion.potions_arr:
            Potion.potions_arr[self.name] = self
