from __future__ import annotations


class Knights:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def from_dict(cls, data: dict) -> Knights:
        name = data["name"]
        power = data["power"]
        hp = data["hp"]

        power += data["weapon"]["power"]

        protection = sum(item["protection"] for item in data["armour"])

        potion = data.get("potion")
        if potion and "effect" in potion:
            eff = potion["effect"]
            power += eff.get("power", 0)
            hp += eff.get("hp", 0)
            protection += eff.get("protection", 0)

        return cls(name, power, hp, protection)
