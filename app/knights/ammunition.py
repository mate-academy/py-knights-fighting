from __future__ import annotations


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def armours_from_dict(
        cls, knight_name: str, knightsConfig: list[dict]
    ) -> list[Armour]:
        knight_dict = knightsConfig[knight_name]
        if knight_dict["armour"]:

            return [
                cls(part=part["part"], protection=part["protection"])
                for part in knight_dict["armour"]
            ]

    def __repr__(self) -> str:
        return f"{{Armour: part={self.part}, protection={self.protection}}}"


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def weapon_from_dict(cls, weapon_dict: dict) -> Weapon:
        return cls(weapon_dict["name"], weapon_dict["power"])


class Potion:
    def __init__(self, name: str, effects: dict) -> None:
        self.name = name
        self.effects = effects

    @classmethod
    def potion_from_dict(cls, potion: dict = None) -> Potion:
        if potion is not None:
            return cls(potion["name"], potion["effect"])
