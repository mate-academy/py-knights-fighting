class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list = None,
            potion: dict = None
    ) -> None:
        self.name = name.title().replace("_", " ")
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = 0

    def total_protection(self) -> int:
        extra_protection = 0

        if self.armour:
            for part_of_armour in self.armour:
                extra_protection += part_of_armour["protection"]

        if self.potion:
            for effect, value in self.potion["effect"].items():
                if effect == "protection":
                    extra_protection += value

        return self.protection + extra_protection

    def total_power(self) -> int:
        extra_power = self.weapon["power"]

        if self.potion:
            for effect, value in self.potion["effect"].items():
                if effect == "power":
                    extra_power += value

        return self.power + extra_power

    def total_hp(self) -> int:
        extra_hp = 0

        if self.potion:
            for effect, value in self.potion["effect"].items():
                if effect == "hp":
                    extra_hp += value

        return self.hp + extra_hp


class KnightBeforeBattle(Knight):
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            protection: int
    ) -> None:
        super().__init__(name, power, hp, {})
        self.protection = protection
