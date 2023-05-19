from typing import Any


class Knight:

    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.human_power = config["power"]
        self.human_hp = config["hp"]
        self.armour = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "human_hp" and value < 0:
            value = 0
        self.__dict__[key] = value
        print(type(self.name))

    def effect_calculation(self, suma: int, attribute: str) -> int:
        if self.potion is not None and self.potion["effect"].get(attribute):
            return suma + self.potion["effect"][attribute]
        return suma

    def protection(self) -> int:
        sum_prot = sum([armour["protection"] for armour in self.armour])
        return self.effect_calculation(
            suma=sum_prot, attribute="protection"
        )

    def power(self) -> int:
        sum_power = self.human_power + self.weapon["power"]
        return self.effect_calculation(
            suma=sum_power, attribute="power"
        )

    def hp(self) -> int:
        return self.effect_calculation(
            suma=self.human_hp, attribute="hp"
        )
