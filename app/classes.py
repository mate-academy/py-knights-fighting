from typing import List, TypedDict


class Armour(TypedDict):
    part: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class Potion(TypedDict):
    name: str
    effect: dict[str, int]


class KnightStats(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion | None


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: List[Armour],
                 weapon: Weapon,
                 potion: Potion | None) -> None:
        self.name = name
        actual_power = power + weapon["power"]
        actual_hp = hp
        actual_protection = 0
        for part in armour:
            actual_protection += part.get("protection", 0)

        if potion is not None:
            for stat, num in potion["effect"].items():
                if stat == "hp":
                    actual_hp += int(num)
                elif stat == "power":
                    actual_power += int(num)
                elif stat == "protection":
                    actual_protection += int(num)

        self.power = actual_power
        self.hp = actual_hp
        self.protection = actual_protection
