from typing import TypedDict


class Armour(TypedDict):
    part: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class Effect(TypedDict):
    hp: int
    power: int
    protection: int


class Potion(TypedDict):
    name: str
    effect: Effect


class Config(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None


class Knight:
    def __init__(self, config: Config) -> None:
        self.name = config["name"]
        self.protection: int = 0
        self.power = config["power"]
        self.hp = config["hp"]
        self.armour: list[Armour] = config["armour"]
        self.weapon = config["weapon"]
        self.potion = config["potion"]

    def set_protection(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def set_power(self) -> None:
        self.power += self.weapon["power"]

    def set_potion(self) -> None:
        if self.potion is not None:

            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
