Armour = [dict]


class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.protection = 0
        self.power = power

    def __str__(self) -> str:
        return (
            f"name: {self.name}, hp: {self.hp}, "
            f"protection: {self.protection}, power: {self.power}"
        )

    def set_protection(self, armours: list[Armour]) -> None:
        for armour in armours:
            self.protection += armour["protection"]

    def set_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def set_potion(self, potion: dict) -> None:
        if potion is not None:
            for key, value in dict(potion["effect"]).items():
                self.__setattr__(key, self.__getattribute__(key) + value)
